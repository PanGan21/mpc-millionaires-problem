from Crypto.Random.random import getrandbits


def oblivious_transfer_alice(m0, m1, n=2048, e=None, d=None, N=None):
    """
    Perform oblivious transfer as Alice.

    Args:
        m0 (int): The first message.
        m1 (int): The second message.
        n (int): The number of bits for RSA parameters (default: 2048).
        e (int): The public exponent (default: None).
        d (int): The private exponent (default: None).
        N (int): The modulus (default: None).

    Yields:
        Tuple[int, int] or int: If e, d, and N are not provided, yields (e, N).
                                 If e, d, and N are provided, yields (x0, x1).
                                 If e, d, and N are provided and v is received, yields (m0k, m1k).

    Raises:
        ValueError: If N is too low.
    """
    if e is None or d is None or N is None:
        e, d, N = gen_rsa_params(n)

    if m0 >= N or m1 >= N:
        raise ValueError('N too low')

    yield (e, N)

    x0, x1 = getrandbits(n), getrandbits(n)

    v = yield (x0, x1)
    k0 = pow(v - x0, d, N)
    k1 = pow(v - x1, d, N)

    m0k = (m0 + k0) % N
    m1k = (m1 + k1) % N

    yield m0k, m1k


def oblivious_transfer_bob(b, n=2048):
    """
    Perform oblivious transfer as Bob.

    Args:
        b (int): The choice bit (0 or 1).
        n (int): The number of bits for RSA parameters (default: 2048).

    Yields:
        None or int: If e and N are received, yields None.
                     If x0 and x1 are received, yields v.
                     If m0k and m1k are received, yields mb.

    Raises:
        ValueError: If b is not 0 or 1.
    """
    if not b in (0, 1):
        raise ValueError('b must be 0 or 1')

    e, N = yield
    x0, x1 = yield

    k = getrandbits(n)
    v = ((x0, x1)[b] + pow(k, e, N)) % N

    m0k, m1k = yield v
    mb = ((m0k, m1k)[b] - k) % N

    yield mb


# 1-2 oblivious transfer
def oblivious_transfer(alice, bob):
    """
    Perform 1-2 oblivious transfer.

    Args:
        alice (generator): The generator function for Alice's side.
        bob (generator): The generator function for Bob's side.

    Returns:
        int: The result of the oblivious transfer.
    """
    e, N = next(alice)
    next(bob)
    bob.send((e, N))

    x0, x1 = next(alice)
    v = bob.send((x0, x1))

    m0k, m1k = alice.send(v)

    mb = bob.send((m0k, m1k))
    return mb
