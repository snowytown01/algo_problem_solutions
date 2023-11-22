import sys


n, m = map(int, sys.stdin.readline().rstrip().split())

mat1 = []
mat2 = []
for i in range(n):
    mat1.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(n):
    mat2.append(list(map(int, sys.stdin.readline().rstrip().split())))

newmat = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        newmat[i][j] = mat1[i][j] + mat2[i][j]

for ele in newmat:
    print(" ".join([str(x) for x in ele]))
