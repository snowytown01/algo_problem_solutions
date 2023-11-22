#들수있는 최대중량
import sys


n = int(sys.stdin.readline())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))
# while True:
#     try:
#         ele = int(sys.stdin.readline().rstrip())
#         ropes.append(ele)
#     except:
#         break
#ropes = [10, 17, 100]
#최소값이 10의 원소개수인3을 곱한값이 최대로들수있는 중량이된다. 30
#10을 제거한다면, 최소값인 17*2 = 34 더 커지게된다.
#17을 제거한다면, 최고삾이 100*1 = 100 이되어 더 커진다.
#즉, 최소값을 하나씩 제거해가면서 가장 큰값을 뽑으면된다.

record = []
ropes.sort(reverse=True)
for i in range(len(ropes)):
    record.append(ropes[i]*(i+1))

print(max(record))
