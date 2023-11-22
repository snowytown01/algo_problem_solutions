import sys


n, k = map(int, sys.stdin.readline().rstrip().split())
data = []
while True:
    try:
        data.append(int(sys.stdin.readline().rstrip()))
    except:
        break

data.reverse()
#data에는 큰숫자부터 작은숫자순으로 배열되어있음.

# result = 0
# for ele in data:
#     while ele <= k:
#         k -= ele
#         result += 1
#그냥 계속 될때까지 빼니까 너무 시간이 오래걸림
#따라서 나눠준다음 그 몫만큼 바로 빼버리도록하고
#몫을 result에 더해주는식으로 재설계

result = 0
for ele in data:
    while ele <= k:
        result += k//ele
        k %= ele

print(result)

