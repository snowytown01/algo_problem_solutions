import sys


n, k = map(int, sys.stdin.readline().rstrip().split())

cnt = 0
while n != 1:
    if n % k != 0:
        n -= 1
        cnt += 1
    else:
        n /= k
        cnt += 1

print(cnt)


#####################

n, k = map(int, sys.stdin.readline().rstrip().split())

cnt2 = 0
while True:
    if n < k:
        break
    target = (n//k)*k
    cnt2 += n-target
    #얼마나 빼줘야하는지가 나옴
    
    n = target
    
    n //= k
    cnt2 += 1

cnt2 += n-1
print(cnt2)
