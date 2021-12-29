from analys import get_binom
from prob import prob
from stream import get_stream, mistakes_num, generate_mistakes, get_distr
from matplotlib import pyplot as pl


def get_mistakes(num, p):
    e = []
    for i in range(num):
        if prob(p):
            e.append(1)
        else:
            e.append(0)
    return e


# def get_binsim_distr(start, end, h, p):
#     result = []
#     i = start
#     while i <= end:
#         stream = get_stream(i)
#         e = get_mistakes(i, p)
#         m_stream = generate_mistakes(stream, e)
#         m_num = mistakes_num(stream, m_stream)
#         pm = m_num/i
#         n = 1000
#         # inums = analys.get_inums(e, n)
#         # print(f'ошибок на {n} бит: ')
#         # print(inums)
#         eps = abs((p-pm)/p)
#         result.append([i, m_num, p, pm, eps])
#         i *= h
#     return result

def get_binsim_distr(stream_len, block_len, p):
    result = []
    stream = get_stream(stream_len)
    e = get_mistakes(stream_len, p)
    m_stream = generate_mistakes(stream, e)
    m_num = mistakes_num(stream, m_stream)

    block_num = int(stream_len / block_len)
    inums = [0] * block_num
    # pm = mistakes_num(stream, m_stream) / stream_len
    k, pm = get_distr(e, block_len)

    return k, pm


if __name__ == '__main__':
    print('Двоично-симметричный канал.')
    # p = float(input('Вероятность ошибки: '))
    p = 0.1

    # dist = get_binsim_distr(100, 100000, 2, p)
    # print('           n    |           i     |           p     |           pi    |        (p-pi)/p ')
    # print('__________________________________________________________________________________________________________')
    # symb = 15
    # for i in dist:
    #     print(f'{i[0]:{symb}} | {i[1]:{symb}} | {i[2]:{symb}} | {i[3]:{symb}} |  {i[4]:{symb}}')
    n = 1000000
    block_len = 100
    binom = get_binom(block_len, p)
    k, pm = get_binsim_distr(n, block_len, p)
    print('  i   | p(i, n) |     pi      ')
    print('____________________________')
    symb = 5
    for i in range(len(k)):
        eps = abs((k[i] - binom[i])/binom[i])
        pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.r')
        print(f'{i:{symb}} | {binom[i]:.8f} | {k[i]:{symb}} | {eps:.8f}')
    pl.show()