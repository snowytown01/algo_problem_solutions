import sys


# a_(n+1) = a_n을 경유지에, n+1을 목적지에, a_n을 목적지에
def hanoi(n, ori, via, dest): #ori, via, dest 는 각상황의 시작,경유,목적지
    if n == 1:
        print(ori, dest)
        return
    
    hanoi(n-1, ori, dest, via)
    print(ori, dest)
    hanoi(n-1, via, ori, dest)


N = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(N):
    cnt = 2*cnt + 1 
    # n더미를 via로 옮기고 다시 dest로 옮기기때문에 2배, n+1을 dest에 옮기기때문에 +1

print(cnt)
hanoi(N, 1, 2, 3)