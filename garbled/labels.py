import itertools
import functools
import operator

from Crypto.Hash import SHA3_256
from Crypto.Util.number import long_to_bytes
from Crypto.Random.random import getrandbits


def combine_keys(keys, k=128):
    """
    Combine multiple keys into a single key using SHA3-256 hash function.

    Args:
        keys (list): A list of integers representing keys.
        k (int): The desired length of the resulting key in bits (default is 128).

    Returns:
        bytes: The combined key.
    """

    h = SHA3_256.new()

    for ki in keys:
        h.update(long_to_bytes(ki))

    return h.digest()


def label_table(output_name, gate, input_names, labels, k=128):
    """
    Label a logic table with cryptographic labels.

    Args:
        logic_table (dict): A dictionary representing the logic table.
        output_name (str): The name of the output variable.
        input_names (list): A list of input variable names.
        k (int): The desired length of the labels in bits (default is 128).

    Returns:
        tuple: A tuple containing the labeled table and the labels dictionary.
    """

    if gate == 'and':
        assert len(input_names) == 2
        logic_table = [[0, 0], [0, 1]]
    elif gate == 'or':
        assert len(input_names) == 2
        logic_table = [[0, 1], [1, 1]]
    elif gate == 'nand':
        assert len(input_names) == 2
        logic_table = [[1, 1], [1, 0]]
    elif gate == 'xnor':
        assert len(input_names) == 2
        logic_table = [[1, 0], [0, 1]]
    elif gate == 'xor':
        assert len(input_names) == 2
        logic_table = [[0, 1], [1, 0]]
    elif gate == 'ornot':
        assert len(input_names) == 2
        logic_table = [[1, 0], [1, 1]]
    elif gate == 'nor':
        assert len(input_names) == 2
        logic_table = [[1, 0], [0, 0]]
    elif gate == 'andnot':
        assert len(input_names) == 2
        logic_table = [[0, 0], [1, 0]]
    elif gate == 'not':
        assert len(input_names) == 1
        logic_table = [1, 0]
    elif gate == 'const_0':
        assert len(input_names) == 0
        logic_table = 0
    elif gate == 'const_1':
        assert len(input_names) == 0
        logic_table = 1
    else:
        raise ValueError('unsupported gate', gate)
    for var in (output_name, *input_names):
        if var not in labels:
            # 0 and 1 labels for each var
            labels[var] = [getrandbits(k), getrandbits(k)]
    labeled_table = []
    for inp_values in itertools.product((0, 1), repeat=len(input_names)):
        output_value = functools.reduce(
            operator.getitem, inp_values, logic_table)
        output_label = labels[output_name][output_value]
        input_labels = [labels[input_name][input_value]
                        for input_name, input_value in zip(input_names, inp_values)]
        labeled_table.append((output_label, input_labels))
    return labeled_table
