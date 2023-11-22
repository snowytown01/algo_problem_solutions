def print_gbp(n, isit_prime):
    # 소수제일 작은것부터 시작해서 주어진n을 완성시킬 짝을 찾고 그짝이 소수인지 판별
    temp = isit_prime.copy()
    # 주의 temp = isit_prime으로 리스트가 복사가된것이 아니다. 메모리 주소가 복사된것이기 때문에 temp가 변경되면
    # isit_prime도 함께 변경이된다 .copy() 메소드를 사용할것
    candid = []

    for i in range(2, 10001):
        if temp[i] == True and temp[n-i] == True:
            candid = [i, n-i]
            temp[i] = False
    
    print(candid[0], candid[1])
    

testcase = int(input())
isit_prime = [False, False] + [True]*9999
for i in range(2, 10001):
    if isit_prime[i]:
        for j in range(2*i, 10001, i):
            isit_prime[j] = False

for i in range(testcase):
    n = int(input())
    
    print_gbp(n, isit_prime)