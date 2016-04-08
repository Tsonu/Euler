def move(x,y,n, count):
  if (x == n and y == n):
    count = count + 1
  if (x != n):
    count = move(x + 1,y,n,count)
  if (y != n):
    count = move(x,y + 1,n,count)
  return count


paths = move(0,0,15,0)
print(paths)
  