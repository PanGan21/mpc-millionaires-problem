from utils import rsa
from oblivious import oblivious_transfer
from utils import symmetric

from .labels import label_table, combine_keys
from .garble_table import garble_table, eval_garbled_table


# X is alice's input
# x = number of bits in the input wire 'x' in the circuit
# y = number of bits in the input wire 'y' in the circuit
# n = RSA security bits
# k = garbled circuits security bits (label size)
def garbled_circuit_alice(circuits, input_wires, output_wires, X, x_bits=32, y_bits=32, n=2048, k=128):
    garbled_tables, labels, wire_index = garble_circuit(
        circuits, input_wires, output_wires)
    output_indexes = [wire_index[wire] for wire in output_wires]

    # {wire_name: [label_0, label_1], ...} -> {label_0: wire_name=0, label_1: wire_name=1, ...}
    labels_to_names = dict((v, k + '=' + str(i))
                           for k, v01 in labels.items() for i, v in enumerate(v01))
    for k, v in labels_to_names.items():
        print(k, '\t', v)

    # setup Alice's input wires
    alice_input_values = {**wire_values('x', X, x_bits)}
    print('alice input values:', alice_input_values)

    # map of wire_index -> given label (for alice's wires)
    alice_input_labels = {wire_index[wire]: labels[wire][alice_input_values[wire]]
                          for wire in input_wires if wire.startswith('x_')}

    # bob also needs to know which wires are his inputs
    bob_input_indexes = [wire_index[f'y_{i}'] for i in range(y_bits)]
    # setup the oblivious transfer for bob's input wires
    ot_alices = []
    e, d, N = rsa.gen_rsa_params(n)
    for i in range(y_bits):
        # get the 0 and 1 labels for bob's input wire 'y'
        m0, m1 = labels[f'y_{i}']
        ot_alices.append(
            oblivious_transfer.oblivious_transfer_alice(m0, m1, n, e, d, N))

    # send parameters to bob and do the oblivious transfer. Bob will reply back with his output labels
    output_labels = yield labels, garbled_tables, alice_input_labels, bob_input_indexes, output_indexes, ot_alices

    # convert the labels back to plain values
    output = [labels_to_names[label] for label in output_labels]
    yield output


# Y is bob's input
# input_bits = number of bits in the input wire 'y' in the circuit
def garbled_circuit_bob(Y, y_bits=32, n=2048, k=128):
    bob_input_values = {**wire_values('y', Y, y_bits)}
    print('bob input values:', bob_input_values)

    # setup the oblivious transfer for bob's input wires
    ot_bobs = [oblivious_transfer.oblivious_transfer_bob(
        bob_input_values[f'y_{i}'], n) for i in range(y_bits)]

    # do the oblivious transfer now. Also, receive the rest of alice's parameters
    garbled_tables, alice_input_labels, bob_input_indexes, output_indexes, bob_input_labels = yield ot_bobs
    assert len(bob_input_indexes) == y_bits and len(bob_input_labels) == y_bits

    # boilerplate, go from a list of label values to a dict from wire to label
    bob_input_labels = dict(zip(bob_input_indexes, bob_input_labels))

    # now we have all the input labels
    input_labels = {**alice_input_labels, **bob_input_labels}
    print('input labels:', input_labels)

    output_labels = eval_garbled_circuit(
        garbled_tables, input_labels, output_indexes)
    yield output_labels


def garble_circuit(circuit, inputs, outputs, k=128):
    labels = {}
    garbled_tables = []

    # we topologically order all the wires. there is a valid topological ordering because circuits are acyclic.
    # by ordering the wires, we can use the indices as unique ids to refer to each wire
    wires = topoorder(circuit, inputs, outputs)
    wire_index = {wire: i for i, wire in enumerate(wires)}

    for wire_name in wires:
        if wire_name in inputs:
            print('input wire:', wire_name)
            # this is an input wire, just add a palceholder value
            garbled_tables.append((None, None))
            continue
        gate, *input_wire_names = circuit[wire_name]
        print(wire_name, gate, input_wire_names)
        labeled_table = label_table(
            wire_name, gate, input_wire_names, labels, k)
        garbled_table = garble_table(labeled_table)

        input_wire_indexes = [wire_index[input_wire]
                              for input_wire in input_wire_names]
        assert all(i < len(garbled_tables) for i in input_wire_indexes)
        garbled_tables.append((garbled_table, input_wire_indexes))

    assert len(garbled_tables) == len(wires)

    return garbled_tables, labels, wire_index


def topoorder(circuit, inputs, outputs):
    postorder = []
    visited = set()

    def visit(wire_name):
        if wire_name in visited:
            return
        visited.add(wire_name)
        if wire_name not in inputs:
            gate, *input_wire_names = circuit[wire_name]
            for input_wire in input_wire_names:
                visit(input_wire)
        postorder.append(wire_name)
    for input_wire in outputs:
        visit(input_wire)
    return postorder  # note: dont need to reverse for topo b.c nodes point to their dependencies


def wire_values(wire_name, value, bitsize):
    bits = bin(value)[2:].zfill(32)
    return {f"{wire_name}_{i}": int(bit) for i, bit in enumerate(reversed(bits))}


def eval_garbled_circuit(garbled_tables, circuit_input_labels, output_wire_indexes):
    # holds an array of the output wire's decrypted label as we progressively evaluate the circuit
    evaluated_gates = []

    for i, (garbled_table, input_wire_indexes) in enumerate(garbled_tables):
        if i in circuit_input_labels:  # this is an input wire
            evaluated_gates.append(circuit_input_labels[i])
            continue

        for row in garbled_table:
            c, tag, nonce = row
            gate_input_labels = [evaluated_gates[index]
                                 for index in input_wire_indexes]
            key = combine_keys(gate_input_labels)
            try:
                output_label = symmetric.symmetric_dec(key, c, tag, nonce)
            except ValueError:  # incorrect padding
                continue
            evaluated_gates.append(output_label)
            break
        else:
            raise ValueError('unable to decrypt garbled table', i)

        print('evaluated gate', i, '=', output_label)

    assert len(evaluated_gates) == len(garbled_tables)

    output_labels = [evaluated_gates[i] for i in output_wire_indexes]
    return output_labels
