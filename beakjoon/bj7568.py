import sys


N = int(input())
data = []
for line in sys.stdin:
    data.append(list(map(int, line.rstrip().split())))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

