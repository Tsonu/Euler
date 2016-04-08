import itertools

def pandigital(n):
  if len(n) != 10:
    return False
  for i in range(10):
    if str(i) not in n:
      return False
  return True

def wack(n):
  test =  ''.join(n[1:4])
  if int(test) % 2 != 0:
    return False
  test =  ''.join(n[2:5])
  if int(test) % 3 != 0:
    return False
  test =  ''.join(n[3:6])
  if int(test) % 5 != 0:
    return False
  test =  ''.join(n[4:7])
  if int(test) % 7 != 0:
    return False
  test =  ''.join(n[5:8])
  if int(test) % 11 != 0:
    return False
  test =  ''.join(n[6:9])
  if int(test) % 13 != 0:
    return False
  test =  ''.join(n[7:10])
  if int(test) % 17 != 0:
    return False
  return True
  
s = "1406357289"
arr = [int(''.join(i)) for i in itertools.permutations(s) if wack(i)]
print arr
print sum(arr)