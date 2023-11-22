def find_index(data, target):
    res = []
    lis = data
    while True:
        try:
            res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0))
            lis = data[res[-1]+1:]
        except:
            break     
    return res

def bm_algorithm(T, P):
    # bad character : 뒤에서부터 하나씩 대조해보다가 아닌거 나오면 P에서 찾고 없으면 밀기
    T_head = 0  # 이하 전부 인덱스
    T_tail = len(P) - 1
    P_head = 0
    P_tail = len(P) - 1

    flag = 0
    broken = 0

    # 근데 하나씩 비교하는것은 코드를 어떻게 짜지 range(P의길이)
    while T_tail <= len(T)-1 and flag == 0:
        for i in range(len(P)):
            if T[T_tail - i] != P[P_tail - i]:
                if T[T_tail - i] in P: # bc가 P에 있을때
                    result = find_index(P, T[T_tail - i])
                    while result[-1] > P_tail - i:
                        result.pop(-1)
                    if len(result) == 0:
                        T_head += P_tail - i + 1
                        T_tail += T_head + len(P) - 1
                        broken = 1
                        break
                    T_head += P_tail - i - result[-1]
                    T_tail += T_head + len(P) - 1
                    broken = 1
                    break
                    

            
                else: # bc가 P에 없을때
                    T_head += P_tail - i + 1
                    T_tail += T_head + len(P) - 1
                    broken = 1
                    break
            
        if(broken != 1):
            flag = 1 # 위의 if문(하나씩비교 break안당하고 끝까지 완료)
    
    print(T_head)

T = 'sdfsadasdhello'
P = 'hello'

bm_algorithm(T, P)

# BM법의 경우에는 초기화를 m으로 다한다음에 k=-1, k=0,1,2 으로 케이스를 나눠서
# 풀어줘야함

def initSkip(p):
    NUM = 27  # 알파벳 수
    M = len(p) # 패턴의 길이
    skip = [M for i in range(NUM)] #skip 함수를 모두 M값으로 초기화
    for i in range(M):
        skip[ord(p[i]) - ord('A')] = M - i - 1 
    return skip # skip 배열 반환

def BM(p, t):
    M = len(p)
    N = len(t)
    skip = initSkip(p)

    i = M-1
    j = M-1

    while j >= 0:
        while t[i] != p[j]:
            k = skip[ord(t[i]) - ord('A')]
            if M - j > k:
                i = i + M - j
            else:
                i = i + k
            if i >= N:
                return N
            j = M - 1
        i = i-1
        j = j-1
    return i+1