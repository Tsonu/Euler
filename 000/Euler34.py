import math
for i in range(3,1000000):
  l = sum([math.factorial(int(j)) for j in str(i)])
  if i == l:
    print l
  