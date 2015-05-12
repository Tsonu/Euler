import EulerMath
def pandigital(n):
  for i in range(1,len(n) + 1):
    if str(i) not in n:
      return False
  return True
i = 1
while i < 100000000:
  if pandigital(str(i)) and EulerMath.isPrime(i):
    print i
  i = i + 1