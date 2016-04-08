import itertools

import EulerMath

primes = EulerMath.primes(10000)
primes2 = EulerMath.primes(1488)
for p in primes:
  if len(str(p)) < 4:
    continue
  arr = []
  for i in itertools.permutations(str(p)):
    j = int(''.join(i))
    if j in primes:
      arr.append(j)
  arr = sorted(list(set(arr)))
#  print arr
  
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      const = arr[j] - arr[i]
      
      if (arr[i] + 2*const) in arr and len(str(arr[i] + 2*const)) == 4:
        print (const, arr[i], arr[i] + const, arr[i] + 2*const)