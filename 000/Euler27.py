import EulerMath
primes = EulerMath.primes(1000)
print primes

limit = 1001
maxN = (0,0,0)
for a in range(-limit,limit):
  for b in range(-limit,limit):
    for n in range(limit):
      value = n*n + b*n + a
      if value not in primes:
        break
      if n > maxN[2]:
        maxN = (a,b,n, abs(a)* abs(b))

print maxN