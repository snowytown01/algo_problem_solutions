# 00:00:00 ~ N:59:59 3을 포함하는 시간의개수
import sys


n = int(sys.stdin.readline().rstrip())

result = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            madestr = str(h) + str(m) + str(s)
            if '3' in madestr: result += 1

print(result)

#완전탐색(브루트포스)은 탐색할 대상이 100만개이하일때 사용하는것이 좋음