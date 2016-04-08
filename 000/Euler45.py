pentagonals = {n*(3*n - 1)/2 for n in range(1,100000)}
hexagonals = {n*(2*n - 1) for n in range(1,100000)}

for i in pentagonals:
  if i in hexagonals:
    print i