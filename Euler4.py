max = 0
for first in range(1,999):
  for second in range(1, 999):
    sum = first * second
    if str(sum) == str(sum)[::-1]:
      if sum > max:
        max = sum
print(max)