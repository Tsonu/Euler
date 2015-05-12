def sumPow(n):
  return sum([int(i)**5 for i in str(n)])

print sum([sumPow(i) for i in range(2,1000000) if sumPow(i) == i])
    