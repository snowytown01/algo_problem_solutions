def print_primecnt(n):
    sign = [False, False] + [True]*(2*n - 1)

    for i in range(2, 2*n + 1):
        if sign[i]:
            for j in range(2*i, 2*n + 1, i):
                sign[j] = False
    
    print(sum(sign[n+1:]))

while True:
    n = int(input())
    if n == 0:
        break

    print_primecnt(n)


