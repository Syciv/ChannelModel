from math import factorial
from stream import get_stream, mistakes_num, generate_mistakes
import numpy as np
import markov as m


def get_blocks(stream):
    blocks = []
    for i in range(int(len(stream) / 4)):
        m = []
        for j in range(4):
            m.append(stream[i * 4 + j])
        blocks.append(np.matrix(m))
    return blocks


def get_codes(blocks, G):
    codes = []
    for m in blocks:
        u = np.mod(m.dot(G), 2)
        codes.append(u)
    return codes


def get_stream_from_codes(codes):
    stream = []
    for i in codes:
        for j in np.array(i)[0]:
            stream.append(j)
    return stream


def get_codes_from_stream(stream):
    codes = []
    for i in range(int(len(stream) / 7)):
        c = []
        for j in range(7):
            c.append(stream[i*7 + j])
        c = np.matrix(c)
        # c = np.squeeze(c)
        codes.append(c)
    return codes


def get_sindroms(codes, H):
    sindroms = []
    for u in codes:
        S = np.mod(H.dot(u.transpose()), 2)
        sindroms.append(S)
    return sindroms


def calc_mistakes(sindroms):
    mistakes = []
    for s in sindroms:
        k = 0
        for i in range(3):
            k += (np.array(s)[2-i][0]*(2**i))
        mistakes.append(k)
    return mistakes


if __name__ == '__main__':
    H = np.matrix([[0, 0, 0, 1, 1, 1, 1],
                   [0, 1, 1, 0, 0, 1, 1],
                   [1, 0, 1, 0, 1, 0, 1]])

    G = np.matrix([[1, 1, 1, 0, 0, 0, 0],
                   [1, 0, 0, 1, 1, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0],
                   [1, 1, 0, 1, 0, 0, 1]])

    n = 4
    stream = get_stream(n)
    print(f'Поток без кодов: {stream}')
    blocks = get_blocks(stream)
    codes = get_codes(blocks, G)
    code_stream = get_stream_from_codes(codes)

    p_good_mistake = 0.28  # float(input('Вероятность ошибки в хорошем состоянии : '))
    p_bad_mistake = 0.7  # float(input('Вероятность ошибки в плохом состоянии: '))
    p_to_good = 0.01  # float(input('Вероятность попасть в хорошее состояние: '))
    p_to_bad = 0.001  # float(input('Вероятность попасть в плохое состояние: '))

    e = m.get_mistakes(len(code_stream), p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    m_stream = generate_mistakes(code_stream, e)

    print(f'Поток с кодами: {code_stream}')
    print(f'Вектор ошибок: {e}')
    print(f'Поток с ошибками: {m_stream}')

    codes = get_codes_from_stream(m_stream)
    sindroms = get_sindroms(codes, H)
    mistakes = calc_mistakes(sindroms)
    print(mistakes)
    # m = np.matrix([0, 0, 1, 1])
    # u = np.mod(m.dot(G), 2)
    # S = np.mod(H.dot(u.transpose()), 2)


