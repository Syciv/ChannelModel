from random import randint, random


def get_stream(n):
    stream = []
    for i in range(n):
        stream.append(randint(0, 1) % 2)
    return stream


def mistakes_num(stream1, stream2):
    num = 0
    for i in range(len(stream1)):
        if stream1[i] != stream2[i]:
                   num += 1
    return num


def generate_mistakes(stream, e):
    result = []
    for i in range(len(stream)):
        result.append((stream[i] ^ e[i]))
    return result