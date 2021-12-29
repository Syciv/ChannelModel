from analys import get_binom
from binsim import get_binsim_distr
from markov import get_markov_distr
from matplotlib import pyplot as pl


if __name__ == '__main__':
    print('Марковская модель.')
    p_good_mistake = 0.1  # float(input('Вероятность ошибки в хорошем состоянии : '))
    p_bad_mistake = 0.2  # float(input('Вероятность ошибки в плохом состоянии: '))
    p_to_good = 0.9  # float(input('Вероятность попасть в хорошее состояние: '))
    p_to_bad = 0.6  # float(input('Вероятность попасть в плохое состояние: '))

    n = 1000000
    block_len = 100
    binom = get_binom(block_len, p_good_mistake)
    k, pm = get_markov_distr(n, block_len, p_good_mistake, p_bad_mistake, p_to_good, p_to_bad)
    for i in range(len(k)):
        # pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.r')

    print(pm)

    n = 1000000
    block_len = 100
    binom = get_binom(block_len, pm)
    k, pmb = get_binsim_distr(n, block_len, pm)
    for i in range(len(k)):
        # pl.plot(i, binom[i], '.b')
        pl.plot(i, k[i], '.g')

    pl.show()

