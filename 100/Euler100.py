target = 10**12
blue = 15
total = 21
while total < target:
    btemp = 3 * blue + 2 * total - 2;
    ttemp = 4 * blue + 3 * total - 3;
    
    blue = btemp
    total = ttemp
print blue, total