exp = [a**b for a in range(100) for b in range(100)]
s = [sum([int(c) for c in str(e)]) for e in exp]
print max(s)