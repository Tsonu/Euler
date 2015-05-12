def collatz(n):
  count = 1
  while (n != 1):
    if (n % 2 == 0):
      n /= 2
    else:
      n = n* 3 + 1
    count = count + 1
  return count

max = 0
for i in range(13,1000001):
  c = collatz(i)
  if (c > max):
    max = c
    print (i,max)
  
