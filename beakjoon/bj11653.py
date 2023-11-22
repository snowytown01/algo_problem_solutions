# N = int(input())

# find prime num < N
# p_num = []

# for i in range(2, N+1):
#     p_num.append(i)
#     for j in range(2, i):
#         if i % j == 0:
#             p_num.pop()
#             break

# for i in p_num:
#     while N % i == 0:
#         print(i)
#         N /= i

# 위 방법은 소인수를 다찾아서 하는것이라 시간이 오래걸림
# 반드시 어떤수의 소인수는 그 어떤수보다 작으니까 다음과같이 해결가능
N = int(input())
n = 2

while N != 1:
    if N % n == 0:
        print(n)
        N /= n
    else:
        n += 1