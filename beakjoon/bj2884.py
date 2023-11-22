def solution(h, m):
    m -= 45
    if m < 0:
        h -= 1
        m += 60
    if h < 0:
        h += 24
    
    print(h, m)

h, m = map(int, input().split())
solution(h, m)