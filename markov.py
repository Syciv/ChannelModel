from prob import prob
from stream import get_stream, mistakes_num, generate_mistakes
from analys import get_binom


def get_mistakes(num, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad):
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


def get_distr(stream_len, block_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad):
    result = []
    k = [0] * block_len

    stream = get_stream(stream_len)
    e = get_mistakes(stream_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    m_stream = generate_mistakes(stream, e)
    m_num = mistakes_num(stream, m_stream)

    block_num = int(stream_len / block_len)
    inums = [0]*block_num

    for i in range(block_num):
        for j in range(block_len):
            if e[i*block_len + j] == 1:
                inums[i] += 1

    for i in inums:
        k[i] += 1

    for i in range(len(k)):
        k[i] /= block_num

    return k


if __name__ == '__main__':
    print('Марковская модель.')
    p_good_mistake = 0.5  # float(input('Вероятность ошибки в хорошем состоянии : '))
    p_bad_mistake = 0.7  # float(input('Вероятность ошибки в плохом состоянии: '))
    p_to_good = 0.01  # float(input('Вероятность попасть в хорошее состояние: '))
    p_to_bad = 0.001  # float(input('Вероятность попасть в плохое состояние: '))

    n = 10000

    binom = get_binom(100, p_good_mistake)
    k = get_distr(10000, 100,  p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    print('           n    |           i     |           p      ')
    print('___________________________________________________')
    symb = 10
    for i in range(len(k)):
        print(f'{i:{symb}} | {binom[i]:{symb}} | {k[i]:{symb}}')
