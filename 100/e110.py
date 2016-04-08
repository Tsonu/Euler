from math import sqrt
import copy
from euler import *
import datetime


def n_from_factorization(factorization):
    return reduce(mul, [x**y for [x, y] in factorization])


def num_divisors(factorization):
    return reduce(mul, [y + 1 for [x, y] in factorization])


def diff_with_increase_at_i(factorization, i):
    current = factorization[i][0] ** factorization[i][1]
    next = factorization[i][0] ** (factorization[i][1] + 2)
    return next - current


def next_factorization(factorization, min_n):
    counter = 0
    test_factorization = copy.deepcopy(factorization)
    this_n = n_from_factorization(test_factorization)

    if this_n >= min_n:
        while this_n >= min_n:
            counter += 1
            if counter >= len(factorization):
                return test_factorization, True
            test_factorization[counter][1] += 2
            for i in range(counter):
                test_factorization[i][1] = test_factorization[counter][1]
            this_n = n_from_factorization(test_factorization)
    else:
        test_factorization[counter][1] += 2

    return test_factorization, False


start = datetime.datetime.now()

# 2**250 is ~ 3**14 which is a good maximum since the number of divs for the first 14 primes > 4e6
min_n = 2**250
n = 2
prime_max = 50
prime_lookup = euler_primes(prime_max)

# start out with the first 5 primes at 2 since, that reduces the initial iterations alot and is a good guess
factorization = [[p, 2 if p < 13 else 0] for p in prime_lookup]
while True:
    num_div = num_divisors(factorization) / 2 + 1
    # print n, n2, num_div, factorization

    if num_div > 4e6:
        # print n, n2, num_div, factorization
        n2 = n_from_factorization(factorization)
        if n2 < min_n:
            n = sqrt(n2)
            min_n = n2
            print 'Result', '%f' % (n), factorization, n2, num_div

    factorization, should_exit = next_factorization(factorization, min_n)
    if should_exit:
        break

print datetime.datetime.now() - start
