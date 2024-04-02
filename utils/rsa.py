from .prime import gen_prime, modinv


def gen_rsa_params(n=2048):
    """
    Generate RSA public and private key parameters.

    Args:
        n (int): The number of bits for the RSA modulus (default is 2048).

    Returns:
        Tuple[int, int, int]: A tuple containing the public exponent (e), private exponent (d), and modulus (N).
    """
    p, q = gen_prime(n//2), gen_prime(n//2)
    N = p * q
    e = 65537
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    return e, d, N
