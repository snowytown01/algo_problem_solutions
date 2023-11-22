def solution(h, m, time):
    m += time
    while m >= 60:
        m -= 60
        h += 1
    while h >= 24:
        h -= 24
    print(h, m)

h, m = map(int, input().split())
time = int(input())

solution(h, m, time)