import sys


cnt = 1

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: 
        global cnt
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    inpstr = sys.stdin.readline().rstrip()
    print(isPalindrome(inpstr), end=' ')
    print(cnt)
    cnt = 1

# 함수안에서 함수밖의전역변수를 사용하려면 해당변수를 gobal로 선언해서 알려준뒤 써야한다.
# gobal variable 처럼(주의, gobal variable += 1 처럼 선언과동시에 조작은불가)