from math import sqrt, trunc

def triangle(n):
  return (n * (n + 1))/2

def countFactors(n):
  count = 0
  initial_n = n
  for i in range (2,int(sqrt(initial_n)) + 1):
    if (n % i is 0):
      count = count + 1
  return count * 2

for i in range(1,50000):
  t = triangle(i)
  c = countFactors(t)
  if (c > 500):
    print (i,t,c)