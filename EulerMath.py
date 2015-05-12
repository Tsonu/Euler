def isPrime(n):
  if n == 1: return False
  if n == 2: return True
  if n == 3: return True
  if n % 2 == 0: return False
  if n % 3 == 0: return False

  i = 5
  w = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += w
    w = 6 - w
  return True

def primes(n):
  return [a for a in range(1,n+1) if isPrime(a)]

def countDivisors(n):
  count = 0
  initial_n = n
  for i in range (2,int(sqrt(initial_n)) + 1):
    if (n % i is 0):
      count = count + 1
  return count * 2

def allDivisors(x):
  divList = []
  y = 1
  while y*y < x:
    if x % y == 0:
      divList.append(y)
      divList.append(int(x / y))
    y += 1
  if y*y == x:
    divList.append(y)
  divList = [i for i in divList if i != x]
  return divList
  
  
def primeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors
  
def primes(n):
    """
    compute the primes below n with the sieve of Eratosthenes
    Time complexity: O(n loglog n). The algorithm requires
    O(n) of memory.
    
    """
    
    ps = []
    sieve = [True] * (n)
    ps.append(2)
    for p in range(3, n, 2):
        if sieve[p]:
            ps.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return ps
  
def distinct_prime_factors(primes_lookup, n):
  """
  returns the number of distinct prime factors
  """
  if n == 1:
    return 0

  count = 0
  for p in primes_lookup:
    if p*p > n:
      break
    if n % p == 0:
      count += 1
      while n % p == 0:
        n /= p
  if n > 1:
    count += 1
  return count