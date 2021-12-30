from random import randint, random

"""Различные функции для работы с потоками бит"""


def get_stream(n):
    """Генерация потока бит длины n"""
    stream = []
    for i in range(n):
        stream.append(randint(0, 1) % 2)
    return stream


def mistakes_num(stream1, stream2):
    """Подсчёт клличества ошибок по двум потокам"""
    num = 0
    for i in range(len(stream1)):
        if stream1[i] != stream2[i]:
                   num += 1
    return num


def generate_mistakes(stream, e):
    """Генерация вектора ошибок"""
    result = []
    for i in range(len(stream)):
        result.append((stream[i] ^ e[i]))
    return result


def get_distr(e, block_len):
    """Подсчёт вероятности количеств ошибок на блоке"""
    stream_len = len(e)
    block_num = int(stream_len / block_len)
    inums = [0] * block_num
    k = [0] * block_len

    for i in range(block_num):
        for j in range(block_len):
            if e[i * block_len + j] == 1:
                inums[i] += 1

    pm = 0
    for i in inums:
        pm +=i
        k[i] += 1
    pm /= block_num
    # print(k)
    for i in range(len(k)):
        k[i] /= block_num
    # print(k)

    return k, pm