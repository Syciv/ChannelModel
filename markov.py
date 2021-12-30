from prob import prob
from stream import get_stream, mistakes_num, generate_mistakes, get_distr
from analys import get_binom_distr
from matplotlib import pyplot as pl

"""Моделированик марковского канала"""


def get_mistakes(num, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad):
    """Генерация вектора ошибок с заданными вероятностями ошибки и переходов состояний"""
    result = []
    state = 1  # 1 - хорошее 0 - плохое
    for i in range(num):
        if prob(p_good_mistake) and state == 1 or prob(p_bad_mistake) and state == 0:
            result.append(1)
        else:
            result.append(0)

        if state == 1:
            if prob(p_to_bad):
                state = 0
        else:
            if prob(p_to_good):
                state = 1
    return result


def get_markov_distr(stream_len, block_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad):
    """Подсчёт вероятности количеств ошибок на блоке"""
    result = []
    stream = get_stream(stream_len)
    e = get_mistakes(stream_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    m_stream = generate_mistakes(stream, e)
    m_num = mistakes_num(stream, m_stream)

    block_num = int(stream_len / block_len)
    inums = [0]*block_num

    # pm = mistakes_num(stream, m_stream) / stream_len
    k, pm = get_distr(e, block_len)

    return k, pm


if __name__ == '__main__':
    print('Марковская модель.')
    p_good_mistake = 0.01  # float(input('Вероятность ошибки в хорошем состоянии : '))
    p_bad_mistake = 0.2  # float(input('Вероятность ошибки в плохом состоянии: '))
    p_to_good = 0.01  # float(input('Вероятность попасть в хорошее состояние: '))
    p_to_bad = 0.01  # float(input('Вероятность попасть в плохое состояние: '))

    n = 100000
    block_len = 100
    binom = get_binom_distr(block_len, p_good_mistake)
    k, pm = get_markov_distr(n, block_len,  p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    print('  n   |     i      |  p      ')
    print('_________________________')
    symb = 5
    for i in range(len(k)):
        pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.r')
        print(f'{i:{symb}} | {binom[i]:.8f} | {k[i]:{symb}}')
    pl.show()