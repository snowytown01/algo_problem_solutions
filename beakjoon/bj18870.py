import sys


N = int(sys.stdin.readline().rstrip())
sortdict = {}

inplist = list(map(int, sys.stdin.readline().rstrip().split()))
inprdup = list(set(inplist))

inprdup.sort()

for i, v in enumerate(inprdup):
    sortdict[v] = i

# k = 0
# for i in inprdup:
#     sortdict[i] = k
#     k += 1

for i in inplist:
    print(sortdict[i], end=' ')

# 위에서 k를써서 인덱스를 구해줬는데 그럴필요없이 enumerate(inprdup)을쓰면
# (인덱스, 값) 으로 튜플을 반환해준다.
# for i, v in enumerate(inprdup):
#   sortdict[v] = i
# 라고하면 k쓸필요없음


