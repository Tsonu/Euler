import math

def pandigital(n):
  if len(n) != 9:
    return False
  for i in range(1,10):
    if str(i) not in n:
      return False
  return True

prod = set()

for i in range(int(math.sqrt(100000000))):
  for j in range(int(math.sqrt(100000000))):
    p = i * j
    st = str(p) + str(i) + str(j)
    if pandigital(st):
      print (st, p)
      prod.add(p)
      
print sum(list(prod))