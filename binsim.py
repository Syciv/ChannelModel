from prob import prob
from stream import get_stream, mistakes_num, generate_mistakes


def get_mistakes(num, p):
    e = []
    for i in range(num):
        if prob(p):
            e.append(1)
        else:
            e.append(0)
    return e


def get_distr(start, end, h, p):
    result = []
    i = start
    while i <= end:
        stream = get_stream(i)
        e = get_mistakes(i, p)
        m_stream = generate_mistakes(stream, e)
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
    print('Двоично-симметричный канал.')
    p = float(input('Вероятность ошибки: '))

    dist = get_distr(100, 100000, 2, p)
    print('           n    |           i     |           p     |           pi    |        (p-pi)/p ')
    print('__________________________________________________________________________________________________________')
    symb = 15
    for i in dist:
        print(f'{i[0]:{symb}} | {i[1]:{symb}} | {i[2]:{symb}} | {i[3]:{symb}} |  {i[4]:{symb}}')

