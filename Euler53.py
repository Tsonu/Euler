import math
def nCr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n - r))
    
count = 0
for n in range (1,101):
    for r in range(1,n+1):
        c = nCr(n,r)
        if c > 10**6:
            print n,r, c
            count = count + 1

print count