import heapq
import sys


n = int(sys.stdin.readline())
h = []

for i in range(n):
    inp = int(sys.stdin.readline().rstrip())

    if inp == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(inp), inp))