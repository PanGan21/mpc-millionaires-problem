import random

from utils import symmetric
from garbled import labels


def garble_table(labeled_table):
    """
    Garble a labeled logic table.

    Args:
        labeled_table (list): A list of tuples containing labeled output and input values.

    Returns:
        list: A list of tuples containing the garbled ciphertext, authentication tag, and nonce for each row in the labeled table.
    """
    result = []

    for row in labeled_table:
        output_label, input_labels = row
        key = labels.combine_keys(input_labels)
        c, tag, nonce = symmetric.symmetric_enc(key, output_label)
        result.append((c, tag, nonce))

    random.shuffle(result)  # this isn't a secure shuffle

    return result


def eval_garbled_table(garbled_table, inputs):
    """
    Evaluate a garbled table using given inputs.

    Args:
        garbled_table (list): A list of tuples representing a garbled table.
                              Each tuple contains two elements: ciphertext and nonce.
        inputs (list): A list of input labels to be used for evaluating the garbled table.

    Returns:
        Any: The output label obtained by evaluating the garbled table with the given inputs.
             If decryption fails for any row in the garbled table, it moves to the next row.
             If all rows fail decryption, None is returned.
    """
    for row in garbled_table:
        ciphertext, nonce = row
        try:
            key = labels.combine_keys(inputs)
            output_label = symmetric.symmetric_dec(key, ciphertext, nonce)
        except ValueError:  # decryption failed, incorrect padding
            continue
        return output_label
