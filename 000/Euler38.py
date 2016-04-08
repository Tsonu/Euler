def pandigital(n):
  if len(n) != 9:
    return False
  for i in range(1,10):
    if str(i) not in n:
      return False
  return True

largest = 0
for i in range(100000):
  l = 0
  s = ""
  for j in range(1, 100):
    s = s + (str(i*j))
    if len(s) is 9 and pandigital(s):
      print i, j, s
      if (int(s) > largest):
        largest = int(s)
      break
print largest