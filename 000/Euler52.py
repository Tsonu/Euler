def match(n):
    if sorted(str(n)) == sorted(str(n*2)) and \
       sorted(str(n)) == sorted(str(n*3)) and \
       sorted(str(n)) == sorted(str(n*4)) and \
       sorted(str(n)) == sorted(str(n*5)) and \
       sorted(str(n)) == sorted(str(n*6)):
           return True
    return False
           
          
for x in range(10**7):
    if match(x):
        print x