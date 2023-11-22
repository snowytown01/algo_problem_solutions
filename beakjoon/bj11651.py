import sys


N = int(sys.stdin.readline().rstrip())
array = []

for i in range(N):
    inplist = list(map(int, sys.stdin.readline().rstrip().split()))
    array.append(inplist)

for i in array:
    i[0], i[1] = i[1], i[0]

array.sort()

for i in array:
    print(i[1], i[0])
