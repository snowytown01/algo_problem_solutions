import sys


n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
for i in range(0, len(data)-1):
    gotnum = data[i]
    for j in range(i+1, len(data)):
        if gotnum != data[j]: result += 1
    
print(result)

#################################################
#위의 방법은 O(n2)라서 비효율적이다.

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

array = [0]*(m+1) #m은 최대무게값
for ele in data:
    array[ele] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n
print(result)