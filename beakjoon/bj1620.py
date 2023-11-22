import sys


n, m = map(int, sys.stdin.readline().rstrip().split())

diction = {}
num = 1
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    diction[name] = num
    diction[num] = name
    num += 1
for _ in range(m):
    inputtemp = sys.stdin.readline().rstrip()
    if inputtemp.isalpha():
        print(diction[inputtemp])
    else:
        print(diction[int(inputtemp)])