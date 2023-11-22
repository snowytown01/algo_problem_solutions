import sys


def fibo(f1, f2, n):
    if n == 0:
        return f1
    elif n == 1:
        return f2
    return fibo(f2, f1+f2, n-1)

n = int(sys.stdin.readline().rstrip())

print(fibo(0, 1, n))

# 위방법은 재귀의 큰수에서 줄여나가는 느낌(탑다운)이 아니라 카운팅하는것같으므로 아래를 추천
# 그거 구할려면 이거이거 필요해요 라고 내던지고 필요한거 구하는건 나중에 맞기는느낌

def fibo2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo2(n-1) + fibo2(n-2)

print(fibo2(n))