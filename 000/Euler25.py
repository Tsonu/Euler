def fib(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a


i = 0
while True:
  f = fib(i)
  l = len(str(f))
  if (l >= 1000):
    print (l,i,f)
    break
  i = i+1
    