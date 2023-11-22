import sys


n = int(sys.stdin.readline())
data = []
# while True:
#     try:
#         temp = sys.stdin.readline().rstrip().split()
#         data.append(list(map(int, temp)))
#     except:
#         break

# for line in sys.stdin:
#     temp = sys.stdin.readline().rstrip().split()
#     data.append(list(map(int, temp)))

for i in range(n):
    temp = sys.stdin.readline().rstrip().split()
    data.append(list(map(int, temp)))


#data를 먼저 끝나는시간이 빠른순으로 소팅해줘야한다
#왜냐하면 빨리끝나는것 먼저해줘야 뒤에 회의를 생각할 경우의수가 많아지니까

#그리고나서 data를 시작하는시간이 빠른순으로 소팅해줘야한다
#왜냐하면 끝나느시간이 같은경우 시작시간과 끝나는시간이 같은녀석이 앞에오게되면
#다른 끝나는시간이같은 놈은 생각을 못해주기때문이다.

data.sort(key= lambda x: (x[1], x[0])) #1인덱스가 끝나는시간

result = 0
endtime = 0
for ele in data:
    if endtime <= ele[0]:
        result += 1
        endtime = ele[1]

print(result)