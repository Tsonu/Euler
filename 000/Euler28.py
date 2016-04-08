sum = 1
count = 1
move = 2
for i in range(501):
  for j in range(4):
    count += move
    sum += count
    print (move +1, count,sum)
  move = move + 2
  
  