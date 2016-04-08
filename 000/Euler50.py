import EulerMath

primes = EulerMath.primes(1000000)
primeSum = [0]
for p in primes:
  primeSum.append(primeSum[-1:][0] + p)
  if primeSum[-1:][0]  in primes:
    print primeSum[-1:][0]
  if primeSum[-1:][0] > 1000000:
    break

      