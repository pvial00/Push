from Crypto.Util import number

def genBase(size):
    A = number.getPrime(size)
    B = number.getPrime(size)
    while B == A:
        B = number.getPrime(size)
    return A, B

def keygen(size):
    A, B = genBase(size)
    N = A * B
    sk = number.getRandomRange(1, (N - 1))
    return sk, N, A

def push_demo(size):
    skA, nA, MA = keygen(size)
    skB, nB, MB = keygen(size)
    U = nA * nB
    S = MA * U
    SB = MB * U
    SS = S * SB
    y = number.getRandomRange(1, (SS - 1))
    yB = number.getRandomRange(1, (SS - 1))
    p1 = pow(y, skA, SS)
    p1B = pow(y, skB, SS)
    print(p1, p1B)
    p2 = pow(p1B, skA, SS)
    p2B = pow(p1, skB, SS)
    print(p2, p2B)
    p3 = pow(yB, skA, p2)
    p3B = pow(yB, skB, p2B)
    print(p3, p3B)
    p4 = pow(p3B, skA, p2)
    p4B = pow(p3, skB, p2B)
    print(p4, p4B)
