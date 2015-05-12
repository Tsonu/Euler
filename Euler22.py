def value(name):
  return sum([ord(c) - ord('A') + 1 for c in name])
  
file = open('Euler22_Names.txt', 'r')
arr = [a.replace("\"","") for a in file.read().split(',')]
arr.sort()

total = 0
for idx, name in enumerate(arr, start=1):
  total += value(name)*idx
  if idx == 938:
    print name, value(name), idx*value(name)
print total