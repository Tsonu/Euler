import timeit
from euler import *
import datetime

start = datetime.datetime.now()
max = 0
n = 2
prime_max = 50
prime_lookup = euler_primes(prime_max)
while True:
    # if n > prime_max:
    #     prime_max *= 10
    #     prime_lookup = euler_primes(prime_max)
    num_divisors = euler_num_divisors(prime_lookup, n**2)
    solutions = num_divisors / 2 + 1
    if solutions > max:
        max = solutions
        print n, n**2, num_divisors, solutions
        print list(euler_prime_factors(prime_lookup, n**2))
    if solutions > 10e2:
        print 'Final: ', n, solutions
        break
    n += 1

print datetime.datetime.now() - start
