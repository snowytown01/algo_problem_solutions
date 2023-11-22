def solution(a, b):
    if a>b:
        print(">")
    elif a<b:
        print("<")
    else:
        print("==")

m, n = map(int, input().split())
solution(m,n)