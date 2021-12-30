from numpy import array
from math import factorial

"""Различные функции для анализа моделей каналов"""


def get_binom_distr(n, p):
    """Биноминальное распределение"""
    result = []
    k = 0
    for k in range(n):
        result.append(get_binom(k, n, p))

    return result


def get_binom(k, n, p):
    """Элемент биномиального распределения для k и n"""
    C = factorial(n) / (factorial(k) * factorial(n - k))
    return C * pow(p, k) * pow(1 - p, n - k)


def get_inums(e, n):
    """Подсчёт количества ошибок на блоках длины n"""
    num = int(len(e) / n)
    result = [0]*num
    for i in range(num):
        for j in range(n):
            if e[i*n + j] == 1:
                result[i] += 1
    return result


def get_s(H, e):
    """Расчёт синдрома"""
    return H.dot(e)


def get_parameters(sindroms, inums, d):
    """Подсчёт ошибочных, обнаруженных и правильных полученных блоков"""
    mistakes = 0
    detected = 0
    correct = 0
    for i in range(len(inums)):
        if inums[i] == 0:
            correct += 1
        elif 0 < inums[i] < d:
            detected += 1
        else:
            s = sindroms[i]
            if s == 0:
                mistakes += 1
            else:
                detected += 1
    return mistakes, detected, correct