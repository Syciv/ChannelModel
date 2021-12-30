from analys import get_binom_distr
from binsim import get_binsim_distr
from markov import get_markov_distr
from matplotlib import pyplot as pl

"""Сравнение марковского канала и дск"""


if __name__ == '__main__':
    print('Марковская модель.')
    p_good_mistake = 0.001  # float(input('Вероятность ошибки в хорошем состоянии : '))
    p_bad_mistake = 0.1  # float(input('Вероятность ошибки в плохом состоянии: '))
    p_to_good = 0.01  # float(input('Вероятность попасть в хорошее состояние: '))
    p_to_bad = 0.01  # float(input('Вероятность попасть в плохое состояние: '))

    n = 100000
    block_len = 100
    binom = get_binom_distr(block_len, p_good_mistake)
    k, pm = get_markov_distr(n, block_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    for i in range(len(k)):
        # pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.r')

    print(pm/100)

    print('Модель двоично-симметричного канала')
    binom = get_binom_distr(block_len, pm/100)
    k, pmb = get_binsim_distr(n, block_len, pm/100)
    for i in range(len(k)):
        # pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.g')

    pl.show()

