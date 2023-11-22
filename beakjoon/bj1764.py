import sys


a = set()
b = set()

n, m = map(int, sys.stdin.readline().rstrip().split())
for _ in range(n):
    a.add(sys.stdin.readline().rstrip())
for _ in range(m):
    b.add(sys.stdin.readline().rstrip())


c = sorted(list(a&b))
print(len(c))
for ele in c:
    print(ele)