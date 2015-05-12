def isPalindrome(i):
  if i == i[::-1]:
    return True
  return False
  
s = 0  
for i in range(1000000):
  b = bin(i)[2:]
  if (isPalindrome(str(i))) and isPalindrome(str(b)):
    print (i,b)
    s += i
    
print s