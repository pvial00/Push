from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    A, B = genBase(size)
    C, K = genBase(size)
    N = A * B
    sk = number.getRandomRange(1, (B - 1))
    return sk, B, N, A

def push_demo(size):
    sk, pk, n, M = keygen(size)
    skB, pkB, nB, MB = keygen(size)
    U = n * nB
    S = M * nB
    SB = MB * n
    p1 = pow(pk, sk, U)
    p1B = pow(pk, skB, U)
    print "p1", p1, p1B
    p2 = pow(p1B, sk, SB)
    p2B = pow(p1, skB, SB)
    print "p2", p2, p2B

push_demo(8)

