def triangle(s):
  total = sum([ord(c) - ord('A') + 1 for c in s])
  if total in triangles:
    return True
  return False

  
triangles = [n*(n + 1)/2 for n in range(1,100)]

file = open('Euler42_Words.txt', 'r')
arr = [a.replace("\"","") for a in file.read().split(',')]
arr.sort()

count = 0
for word in arr:
  if triangle(word):
    count = count + 1
print count