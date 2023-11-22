import sys


_ = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

result = 0
subsum = 0
for ele in data:
    subsum += ele
    result += subsum

print(result)