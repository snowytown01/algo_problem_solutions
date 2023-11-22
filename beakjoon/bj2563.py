import sys


paper = [[0]*100 for _ in range(100)]

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    for xi in range(x, x+10):
        for yi in range(y, y+10):
            paper[xi][yi] = 1

result = 0
for ele in paper:
    result += sum(ele)
print(result)
