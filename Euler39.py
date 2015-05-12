import math

m = 0
maxP = 0
for p in range(2,1001,2):
  count = 0
  for a in range(2,int (p/3)):
    if (p*(p-2*a) %(2*p-a)) == 0:
      print (p,a)
      count = count + 1
  if count > m:
    m = count
    maxP = p
print (maxP, m)