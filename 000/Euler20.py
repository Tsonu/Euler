fact = 1
for i in range (1,101):
  fact *= i

str_fact = str(fact)
sum_total = 0
for i in range(len(str_fact)):
  sum_total += int(str_fact[i])
  
  print sum_total