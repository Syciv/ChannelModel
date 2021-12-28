from numpy import array
from math import factorial


def get_binom(n, p):
    result = {}
    k = 0
    for k in range(n):
        C = factorial(n) / (factorial(k) * factorial(n - k))
        result[k] = (C * pow(p, k) * pow(1 - p, n - k))

    return result


def get_inums(e, n):
    num = int(len(e) / n)
    result = []
    for i in range(num):
        result.append(0)
        for j in range(n):
            if e[i*n + j] == 1:
                result[i] += 1
    return result


def get_s(H, e):
    return H.dot(e)


def get_parameters(e, block_len, d, H):
    inums = get_inums(e, block_len)
    mistakes = 0
    detected = 0
    correct = 0
    for i in inums:
        if i == 0:
            correct += 1
        elif 0 < i < d:
            detected += 1
        else:
            s = get_s(H, e)
