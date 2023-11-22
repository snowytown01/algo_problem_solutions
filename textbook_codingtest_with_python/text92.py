import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
numlist = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
cnt = 0
deleted = 0
while M != 0:
    M -= 1
    cnt += 1
    if cnt == K+1:
        cnt = 0
        deleted = max(numlist)
        numlist.remove(deleted)
    result += max(numlist)
    if cnt == 0:
        numlist.append(deleted)

print(result)

# 66 5 66 5 66       36 10 46
# 6 5 6 5 6 5 6 5    24 20 44

N, M, K = map(int, sys.stdin.readline().rstrip().split())
numlist.sort()
first = numlist[N-1]
second = numlist[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)

######################
N, M, K = map(int, sys.stdin.readline().rstrip().split())

count = (M // (K+1)) * K #전체결과의 K개의가장큰수1개의그다음큰수조합의수열K+1이 몇개들어갈지 확인하고 각수열안에 K개의가장큰수
count += M % (K+1)

result = 0
result += count * first
result += (M-count) * second

print(result)