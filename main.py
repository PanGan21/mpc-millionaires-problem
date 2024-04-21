from circuit import parser
from garbled import garbled_circuit
from oblivious import oblivious_transfer


if __name__ == "__main__":
    # build with yosys -s ./circuit/yosys-generate-out.txt
    circuit, input_wires, output_wires = parser.parse_verilog("circuit/out.v")

    X = 9001
    Y = 1337

    # setup
    gc_alice = garbled_circuit.garbled_circuit_alice(
        circuit, input_wires, output_wires, X, x_bits=32, y_bits=32)
    gc_bob = garbled_circuit.garbled_circuit_bob(Y, y_bits=32)

    # alice garbles the circuit and prepares for an oblivious transfer of bob's input labels
    labels, garbled_tables, alice_input_labels, bob_input_indexes, output_indexes, ot_alices = next(
        gc_alice)
    # bob prepares for an oblivious transfer of all his input labels
    ot_bobs = next(gc_bob)

    # do the oblivious transfer of all of bobs input wire bits
    bob_input_labels = [oblivious_transfer.oblivious_transfer(
        alice, bob) for alice, bob in zip(ot_alices, ot_bobs)]
    print('bob input labels:', bob_input_labels)

    # Send bob all the other params from Alice too
    # then Bob will run the garbled circuit
    output_labels = gc_bob.send(
        (garbled_tables, alice_input_labels, bob_input_indexes, output_indexes, bob_input_labels))
    print('output labels:', output_labels)

    # give output labels to alice to get final output
    output = gc_alice.send(output_labels)
    for val in output:
        print(val)

    exit()
