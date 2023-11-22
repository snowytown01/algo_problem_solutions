def solution(a, b):
    print(a + b)

iter = int(input())

for i in range(iter):
    a, b = map(int, input().split())
    solution(a, b)
