N = int(input())
n = 1

while n*(n+1)/2 < N:
    n += 1

# 갱신된 n이 N이 속한 부분열 번호임

row = n

# 해당부분열의 몇번째 원소인가

order_row = N - n*(n-1)/2

if row % 2 != 0: # 부분열의 넘버가 홀수일때
    up = row
    down = 1

    while order_row != 1:
        order_row -= 1
        up -= 1
        down += 1
else: # 부분열의 넘버가 짝수일때
    up = 1
    down = row

    while order_row != 1:
        order_row -= 1
        up += 1
        down -= 1

print(str(up) + "/" + str(down))