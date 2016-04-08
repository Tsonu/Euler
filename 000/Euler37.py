import EulerMath

def truncate(s, d):
  if (d == "l"):
    s = s[1:]
  else:
    s = s[:-1]
  return s

arr = []
for i in range(10,1000000):
  test = str(i)
  isPrime = True
  numbers = len(test)
  for n in range(numbers):
    if not EulerMath.isPrime(int(test)):
      isPrime = False
    test = truncate(test, "l")
  test = str(i  )
  for n in range(numbers):
    if not EulerMath.isPrime(int(test)):
      isPrime = False
    test = truncate(test, "r")
  if isPrime:
    print i
    arr.append(i)
    
print arr
print len(arr)
print sum(arr)
    