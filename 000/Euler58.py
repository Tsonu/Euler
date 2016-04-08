import EulerMath
primes = EulerMath.primes(10 ** 7)

total = 1
primeCount = 0
for i in range(2,10**6,2):
    x = i
    n1 = x*x - x + 1
    n2 = x*x + 1
    x = x + 1
    n3  = x*x - x + 1
    n4 = x*x
    
    total = total + 4
    if n1 in primes:
        primeCount = primeCount + 1
    if n2 in primes:
        primeCount = primeCount + 1
    if n3 in primes:
        primeCount = primeCount + 1
    if n4 in primes:
        primeCount = primeCount + 1
    ratio = float(primeCount)/float(total)
        
    print i, primeCount, total, ratio
    if ratio < 0.1:
        break
    
        
        