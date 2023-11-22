import sys


n = int(sys.stdin.readline().rstrip())

roads = list(map(int, sys.stdin.readline().rstrip().split()))
costs = list(map(int, sys.stdin.readline().rstrip().split()))

result = roads[0] * costs[0]
m = costs[0]
dist = 0

for i in range(1, n-1):
    if costs[i] < m:
        result += m*dist
        dist = roads[i]
        m = costs[i]
    else:
        dist += roads[i]
        
    if i == n-2:
        result += m*dist

print(result)