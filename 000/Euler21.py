import math

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
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
  
def find_all_divisors(x):
    divList = []
    y = 1
    while y*y < x:
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    divList = [i for i in divList if i != x]
    return divList


total = 0
for i in range(10001):
  f = find_all_divisors(i)
  s = sum(f)
  f2 = find_all_divisors(s)
  if sum(f2) == i and s != i:
    total += i
    print (i,f,s,f2, sum(f2))
print total