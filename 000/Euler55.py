def palindrome(n):
    if (str(n) == str(n)[::-1]):
        return True;
    return False;
    
def lychral(n):
    for i in range(50):
        r = int(str(n)[::-1])
        if palindrome(n + r):
            return False;
        n = r + n
    return True;
    
    
count = 0
for i in range(10**4 + 1):
    if (lychral(i)):
        count = count + 1
        print i
print count