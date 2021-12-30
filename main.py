from stream import get_stream, generate_mistakes
import numpy as np
import markov as m
import binsim as b
from analys import get_inums, get_parameters, get_binom


def get_blocks(stream, n):
    """Разделение потока на блоки по n бит"""
    blocks = []
    for i in range(int(len(stream) / n)):
        m = []
        for j in range(n):
            m.append(stream[i * n + j])
        blocks.append(np.matrix(m))
    return blocks


def get_codes(blocks, G):
    """Формирование кодов Хемминга по матрице G"""
    codes = []
    for m in blocks:
        u = np.mod(m.dot(G), 2)
        codes.append(u)
    return codes


def get_stream_from_codes(codes):
    """Формирование потока из множества блоков"""
    stream = []
    for i in codes:
        for j in np.array(i)[0]:
            stream.append(j)
    return stream


def get_codes_from_stream(stream, n):
    """Формирование матриц длины n из потока"""
    codes = []
    for i in range(int(len(stream) / n)):
        c = []
        for j in range(n):
            c.append(stream[i*n + j])
        c = np.matrix(c)
        # c = np.squeeze(c)
        codes.append(c)
    return codes


def get_sindroms(codes, H):
    """Расчёт синдромов для блоков по пораждающей матрице H"""
    sindroms = []
    for u in codes:
        S = np.mod(H.dot(u.transpose()), 2)
        sindroms.append(S)
    return sindroms


def calc_sindroms(sindroms):
    """Подсчёт чисел в синдроме по матрицам"""
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

    num = 100000

    n = 7
    d = 3
    k = 4

    stream = get_stream(num)
    # print(f'Поток без кодов: {stream}')
    blocks = get_blocks(stream, k)
    codes = get_codes(blocks, G)
    code_stream = get_stream_from_codes(codes)

    p = 0.15

    e = b.get_mistakes(len(code_stream), p)
    m_stream = generate_mistakes(code_stream, e)

    codes = get_codes_from_stream(m_stream, n)
    sindroms = get_sindroms(codes, H)
    inums = get_inums(e, 7)
    sindroms_num = calc_sindroms(sindroms)

    mistakes, detected, correct = get_parameters(sindroms_num, inums, 3)
    print(f'Ошибочно: {mistakes}, Обнаружено: {detected}, Правильно: {correct}')

    pm_exp = mistakes / (num/4)
    pd_exp = detected / (num/4)
    pc_exp = correct / (num/4)

    pm_th = sum([get_binom(i, 7, p) for i in range(4, 8)])
    pd_th = sum([get_binom(i, 7, p) for i in range(1, 3)])
    pc_th = (1-p)**7
    print("       Теор. | Эксп.")
    print(f'Pош: {pm_th:.5f} | {pm_exp:.5f}')
    print(f'Pоб: {pd_th:.5f} | {pd_exp:.5f}')
    print(f'Pпр: {pc_th:.5f} | {pc_exp:.5f}')



