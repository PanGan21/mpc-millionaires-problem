import itertools
import functools
import operator
import random

from Crypto.Hash import SHA3_256
from Crypto.Util.number import getRandomNBitInteger, long_to_bytes

from .symmetric import symmetric_enc


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


def label_table(logic_table, output_name, input_names, k=128):
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

    labels = {}

    # generate 0 and 1 labels for each var
    for var in (output_name, *input_names):
        labels[var] = [getRandomNBitInteger(k), getRandomNBitInteger(k)]

    labeled_table = []
    # some itertools b.s. to support arbitrary number of input wires
    # number of input wires = number of dimensions of the logic table
    for inp_values in itertools.product((0, 1), repeat=len(input_names)):
        output_value = functools.reduce(
            operator.getitem, inp_values, logic_table)
        output_label = labels[output_name][output_value]
        input_labels = [labels[input_names[i]][v]
                        for i, v in enumerate(inp_values)]
        labeled_table.append((output_label, input_labels))

    return labeled_table, labels


def garble_table(labeled_table):
    result = []
    for row in labeled_table:
        output_label, input_labels = row
        key = combine_keys(input_labels)
        c, tag, nonce = symmetric_enc(key, output_label)
        result.append((c, tag, nonce))

    random.shuffle(result)  # this isn't a secure shuffle

    return result
