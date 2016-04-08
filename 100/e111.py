import datetime

def bouncy(n):
    up = False
    down = False
    s = str(n)

    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            up = True
        elif s[i] < s[i-1]:
            down = True
    return up and down


start = datetime.datetime.now()
num_bouncy = 0
i = 10
while True:
    if bouncy(i):
        num_bouncy += 1
    if float(num_bouncy)/float(i) > 0.99:
        print 'Final', i, float(num_bouncy)/float(i)
        break
    i += 1

print datetime.datetime.now() - start