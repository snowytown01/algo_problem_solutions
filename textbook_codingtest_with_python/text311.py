import sys


n = int(sys.stdin.readline().rstrip())
afraidlist = list(map(int, sys.stdin.readline().rstrip().split()))

afraidlist.sort()
# 1 3 4 5
# 맨앞거 하나잡고 앞에서부터 그맨앞거보다 작거나같은 숫자를 찾고 그 숫자가 자기포함 자기숫자와 같아질때 그 숫자까지 삭제하고 카운트업

cnt = 0
cursor = 0

while True:
    flag = 0
    cought = afraidlist[cursor]

    tempmeter = 0
    for ele in afraidlist:
        if ele <= cought: tempmeter += 1
        if tempmeter == cought:
            cnt += 1
            afraidlist = afraidlist[tempmeter:]
            cursor = 0
            flag = 1
            break
    if flag == 0: cursor += 1
        
    print(cought)    
    print(afraidlist)
    #아래if문에서 리스트가 비어있는경우는

    if len(afraidlist) < cought:
        break

print(cnt)

##############################################

n = int(sys.stdin.readline().rstrip())
afraidlist = list(map(int, sys.stdin.readline().rstrip().split()))

afraidlist.sort()

result = 0
count = 0

for i in afraidlist:
    count += 1
    if count == i:
        result += 1
        count = 0

print(result)



