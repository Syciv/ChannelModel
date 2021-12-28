import sys
from math import factorial
from random import randint, random
from prob import prob
import binsim
import markov
import analys


def get_stream(n):
    stream = ''
    for i in range(n):
        stream += str(randint(0, 1) % 2)
    return stream


def mistakes_num(stream1, stream2):
    num = 0
    for i in range(len(stream1)):
        if stream1[i] != stream2[i]:
                   num += 1
    return num


def get_binom(n, p):
    result = {}
    k = 0
    for k in range(n):
        C = factorial(n) / (factorial(k) * factorial(n - k))
        result[k] = (C * pow(p, k) * pow(1 - p, n - k))

    return result


def get_distr(start, end, h, p):
    result = []
    i = start
    while i <= end:
        stream = get_stream(i)
        e = binsim.get_mistakes(i, p)
        m_stream = binsim.generate_mistake(stream, e)
        m_num = mistakes_num(stream, m_stream)
        pm = m_num/i
        n = 1000
        # inums = analys.get_inums(e, n)
        # print(f'ошибок на {n} бит: ')
        # print(inums)
        eps = abs((p-pm)/p)
        result.append([i, m_num, p, pm, eps])
        i *= h
    return result
        

if __name__ == '__main__':
    # print('Двоично-симметричный канал.')
    # p = float(input('Вероятность ошибки: '))
    # if p > 1 or p < 0:
    #     print('Нельзя...')
    #     sys.exit()
    #
    # dist = get_distr(100, 100000, 2, p)
    # print('           n    |           i     |           p     |           pi    |        (p-pi)/p ')
    # print('__________________________________________________________________________________________________________')
    # symb = 15
    # for i in dist:
    #     pyplot.plot(i[0], i[4], "b.")
    #     print(f'{i[0]:{symb}} | {i[1]:{symb}} | {i[2]:{symb}} | {i[3]:{symb}} |  {i[4]:{symb}}')

    print('Марковская модель.')
    p1 = float(input('Вероятность ошибки, если не было : '))
    p2 = float(input('Вероятность ошибки, если была: '))

    n = 10000

    stream = get_stream(n)
    m_e = markov.get_mistakes(n, p1, p2)
    markov_stream = binsim.generate_mistake(stream, m_e)
    m_num = mistakes_num(stream, markov_stream)
    pm = m_num / n

    # block_len = int(n / 100)
    # inums = analys.get_inums(m_e, block_len)

    # print(inums)

    print(f'Битов: {n}, Ошибок: {m_num}')
    print(f'Оценка вероятности ошибки: {pm}')
