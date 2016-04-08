fac = 2**1000
factStr = str(fac)
sum = 0
for i in range(0,len(factStr)):
  sum += int(factStr[i])
  
print(sum)