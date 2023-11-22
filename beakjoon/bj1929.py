# M, N = map(int, input().split())
# sqrt_N = N ** (1/2)

# # 1~N의 숫자리스트 생성
# num_list = [i for i in range(1, N+1)]

# # 숫자리스트에서 체로 걸러내기
# num_list.remove(1)

# seednum = 2
# index_seednum = 0
# multiplier = 2
# composite = seednum * multiplier

# while seednum <= sqrt_N:
#     while composite <= N:
#         try:
#             num_list.remove(composite)
#         except ValueError:
#             pass
#         multiplier += 1
#         composite = seednum * multiplier
#     index_seednum += 1
#     seednum = num_list[index_seednum]
#     multiplier = 2
#     composite = seednum * multiplier

# # 1~M-1의 소수를 제거
# temp = num_list[0]
# index_temp = 0
# while temp < M:
#     index_temp += 1
#     temp = num_list[index_temp]

# for i in num_list[index_temp:]:
#     print(i)

# 위의 방법은 앞의것 잡고 그 배수를 전부 리스트에서 제거해주는것인데
# remove연산이 너무 많아짐 처음부터 하나하나 탐색해야되니까

M, N = map(int, input().split())

isit_prime = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if isit_prime[i]:
        primes.append(i)
        for j in range(i*2, N+1, i): # 소수라고 판단된 i의 배수는 i+i(2배수), i+i+i(3배수), ... 이므로 range의 공차를 이용해 표현가능
            isit_prime[j] = False

found_index = -1
for i in primes:
    found_index += 1
    if i >= M:
        break

for i in primes[found_index:]:
    print(i)