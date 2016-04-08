import EulerMath


def abundantNumbers(n):
  abundant = []
  for i in range(2,n):
    s = sum(EulerMath.allDivisors(i))
    if s > i:
      abundant.append(i)
  return abundant

def E23():
  limit = 25000
  abundant = abundantNumbers(limit)  
  possibles = set()
  i = 0
  for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
      try:
        if abundant[i] + abundant[j] <= limit:
          possibles.add(abundant[i] + abundant[j])
        else:
          break
      except IndexError:
        print (i,j)
  
  print sum(set(range(1,limit)).difference(possibles))
    
 
E23()