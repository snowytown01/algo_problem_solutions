N = int(input())
array = list(map(int, input().split()))
n = int(input())

cnt = 0
for i in array:
    if i == n:
        cnt += 1

print(cnt)

# 파이썬에서 리스트내 요소의 개수를 구할때는 count메소드를 사용하면된다.
# array.count(n)