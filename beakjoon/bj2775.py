def add_recur(i, j):
    if i == 0:
        return j
    if j == 1:
        return 1
    
    return add_recur(i, j-1) + add_recur(i-1, j)

def add_iter(i, j): #i층, j호 => i-1층까지 모든 칸을 채우고 i-1층의 원소를 전부합
    arr = [[0]*(j+1) for _ in range(i+1)] # 시작이인덱스0이고, 끝이i,j로끝나게끔
    for k in range(j+1):
        arr[0][k] = k
    for l in range(i+1):
        arr[l][1] = 1
    
    for k in range(1, i): #i-1인덱스까지만 계산하기
        for l in range(2, j+1):
            arr[k][l] = arr[k][l-1] + arr[k-1][l]
    
    result = 0
    for m in range(j+1):
        result += arr[i-1][m]
    print(result)   

    

test_case = int(input())
for i in range(test_case):
    k = int(input())
    n = int(input())

    add_iter(k, n)


# 다음과같이 일차원리스트에 앞에것이 갱신되어 올라가는것을 이용해서 일차원리스트를 갱신해나가는것을이용할수있음
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력


# 리스트[] 로 접근할때 슬라이싱이용하면 편리
# list[:6] 이라고하면 인덱스 0~5까지를 가리키게됨
# list[:6:2] 라고하면 공차가2가됨 먼저 0인덱스출력하고 공차2씩 인덱스 더해감