from sys import exit

def p(n):
    return n * (3 * n - 1) / 2 

pentagonals = set()
n = 1 
k = 2 
while True:
    while p(n) < p(k) + p(k - 1): 
        pentagonals.add(p(n))
        n += 1
    for j in range(1, k): 
        if p(k) - p(j) in pentagonals and p(k) + p(j) in pentagonals:
            print p(k) - p(j)
            exit()
    k += 1