from collections import Counter
from operator import mul

def euler_primes(n):
    ps = []
    sieve = [True] * n
    ps.append(2)
    for p in range(3, n, 2):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return ps


def euler_prime_factors(primes_lookup, n):
    for p in primes_lookup:
        if p*p > n:
            break
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n


def euler_distinct_prime_factors(primes_lookup, n):
    if n == 1:
        return 0

    count = 0
    for p in primes_lookup:
        if p * p > n:
            break
        if n % p == 0:
            count += 1
            while n % p == 0:
                n /= p
    if n > 1:
        count += 1
    return count

def euler_num_divisors(prime_lookup, n):
    factor_list = Counter(euler_prime_factors(prime_lookup, n))
    return reduce(mul, [y + 1 for [x, y] in factor_list.items()])

def euler_all_divisors(prime_lookup, n):
    factor_list = Counter(euler_prime_factors(prime_lookup, n))
    factors = factor_list.keys()
    count = factor_list.values()
    num_factors = count_generator(factors)
    f = [0] * num_factors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x]**f[x] for x in range(num_factors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= count[i]:
                break
            f[i] = 0
            i += 1
            if i >= num_factors:
                return


def count_generator(gen):
    return sum(1 for _ in gen)
