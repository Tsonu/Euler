import EulerMath
primes = {i for i in range(2,10000) if EulerMath.isPrime(i)}
squares = {i*i for i in range(1,1000)}

for i in range(1,10000,2):
  if i in primes: continue
  goldbach = True
  for j in primes:
    d = (float(i) - float(j))/2
    if d in squares: goldbach = False
  if goldbach: print i