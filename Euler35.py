import EulerMath

def rotate(i):
  s = str(i)
  s = (s[len(s) - 1]) + s
  s = s[:-1]
  return int(s)

arr = []
for i in range(1000000):
  test = i
  isPrime = True
  for n in range(len(str(test))):
    if not EulerMath.isPrime(test):
      isPrime = False
    test = rotate(test)
  if isPrime:
    print i
    arr.append(i)
    
print len(arr)
    