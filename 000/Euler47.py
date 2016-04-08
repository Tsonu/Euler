import EulerMath

primes = EulerMath.primes(1000000)
for i in range (10000000):
  if EulerMath.distinct_prime_factors(primes, i) == 4 and EulerMath.distinct_prime_factors(primes, i + 1) == 4 and EulerMath.distinct_prime_factors(primes, i + 2) == 4 and EulerMath.distinct_prime_factors(primes, i + 3) == 4:
    print i
  