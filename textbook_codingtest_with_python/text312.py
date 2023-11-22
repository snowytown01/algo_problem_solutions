import sys


inputstr = sys.stdin.readline().rstrip()


initnum = int(inputstr[0])

for i in range(1, len(inputstr)):
    if initnum <= 1 or int(inputstr[i]) <= 1:
        initnum += int(inputstr[i])
    else:
        initnum *= int(inputstr[i])

print(initnum)