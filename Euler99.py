import math
file = open('Euler99_words.txt', 'r')
arr = [a.split(',') for a in file.read().split('\n')]
exp = [float(a[1])*math.log(float(a[0])) for a in arr]

m =  max(exp)
index = exp.index(m)

print index, index + 1, exp[index], arr[index]
