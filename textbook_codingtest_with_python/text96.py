import sys

numlist = []    
n, m = map(int, sys.stdin.readline().rstrip().split())
for i in range(n):
    numlist.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = []
for li in numlist:
    result.append(min(li))

print(max(result))