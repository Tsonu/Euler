def expand(n):
    num = 1
    dem = 2
    for i in range(n):
        temp = num + 2 * dem
        num = dem
        dem = temp
    if len(str(num + dem)) > len(str(dem)):
        return True
    return False
    
count = 0
for x in range(1000):
    if expand(x):
        print x
        count = count + 1
        
print count