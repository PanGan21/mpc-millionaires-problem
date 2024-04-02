from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long


def symmetric_enc(key, x):
    """
    Encrypt an integer using AES in CTR mode.

    Args:
        key (bytes): The encryption key.
        x (int): The integer to be encrypted.

    Returns:
        tuple: A tuple containing the ciphertext bytes, the authentication tag and the nonce.
    """
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(pad(long_to_bytes(x), 16))
    nonce = cipher.nonce
    return ciphertext, tag, nonce


def symmetric_dec(key, ciphertext, nonce):
    """
    Decrypt ciphertext using AES in CTR mode.

    Args:
        key (bytes): The decryption key.
        ciphertext (bytes): The ciphertext bytes.
        nonce (bytes): The nonce used during encryption.

    Returns:
        int: The decrypted integer.
    """
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    x = bytes_to_long(unpad(cipher.decrypt(ciphertext), 16))
    return x
