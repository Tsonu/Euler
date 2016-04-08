def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
  
def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    return (numer / common_divisor, denom / common_divisor)

num = [(1,1) for i in range(10)]
l = 0
for i in range(10,100):
  for j in range(10,100):
    reduced = (int(str(i)[0]), int(str(j)[1]))
    if  reduced[0] != 0 and reduced[1] != 0 and float(i)/float(j) == float(reduced[0])/float(reduced[1]) and int(str(i)[0]) != int(str(i)[1]) and int(str(i)[1]) == int(str(j)[0]):
      print (i,j,reduced, i/j, float(i)/float(j), float(reduced[0])/float(reduced[1]))
      num[l] = (i,j)
      l = l + 1
      
prod = [1,1]
for x in num:
  prod[0] = x[0]*prod[0]
  prod[1] = x[1]*prod[1]
  print prod
  
lowest = simplify_fraction(prod[0],prod[1])
print lowest