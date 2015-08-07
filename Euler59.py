import itertools

file = open('Euler59_Words.txt', 'r')
arr = [a for a in file.read().split(',')]

file2 = open('dict.txt')
words = [a.lower() for a in file2.read().split('\n')]
words.remove('')

for key in itertools.permutations('abcdefghijklmnopqrstuvwxyz', 3):
    temp = ""
    for i in range(len(arr)):
        temp = temp + (chr(int(arr[i]) ^ int(ord(key[i%3]))))
    decrypt = temp.split(' ')

    if len(decrypt) > 10:
        if decrypt[0] in words or decrypt[2] in words or decrypt[3] in words or decrypt[4] in words:
            print key, temp
            print sum([int(ord(a)) for a in temp])
            raw_input()
