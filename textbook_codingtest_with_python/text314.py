import sys


_ = input()
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)



