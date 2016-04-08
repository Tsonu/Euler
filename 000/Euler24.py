from math import factorial

z = 1000000-1
digits = "0123456789"
result = ""

while digits:
	d = len(digits)-1
	t = z/factorial(d)
	result += digits[t]
	z = z%factorial(d)
	digits = digits[:t] + digits[t+1:]

print result
  