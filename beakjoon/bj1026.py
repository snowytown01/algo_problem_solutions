import sys


_ = sys.stdin.readline()
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
b.sort()
b.reverse()

result = 0
for i in range(len(a)):
    result += a[i]*b[i]

print(result)
