import sys



a = set()
b = []

n, m = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    a.add(sys.stdin.readline().rstrip())
for i in range(m):
    b.append(sys.stdin.readline().rstrip())

cnt = 0
for i in b:
    if i in a: cnt += 1

print(cnt)