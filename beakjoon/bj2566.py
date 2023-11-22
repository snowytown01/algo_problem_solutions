import sys


table = []
for i in range(9):
    table.append(list(map(int, sys.stdin.readline().rstrip().split())))
initone = (table[0][0], 0, 0)
for i in range(9):
    for j in range(9):
        if table[i][j] >= initone[0]:
            initone = (table[i][j], i, j)

print(initone[0])
print(initone[1]+1, initone[2]+1)