import datetime
from math import sqrt

def fibonacci(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


start = datetime.datetime.now()

fibs = []
for i in range(2,101):
    fibs.append(int(fibonacci(i)))

print fibs

print datetime.datetime.now() - start