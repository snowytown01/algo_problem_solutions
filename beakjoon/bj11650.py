import sys


N = int(sys.stdin.readline().rstrip())
array = []

for i in range(N):
    inp_list = list(map(int, sys.stdin.readline().rstrip().split()))
    array.append(inp_list)

array.sort()

for i in range(N):
    print(array[i][0], array[i][1])

