#먼저 모든 앞0을 없애주는것부터시작
import sys


# inputstr = sys.stdin.readline().rstrip()

# insertplace = []
# closepar = -1
# for idx in range(len(inputstr)):
#     if closepar == -1 and inputstr[idx] == '-':
#         closepar = idx
#     if closepar != -1 and inputstr[idx] == '-':
#         insertplace.append((closepar, idx))
#         closepar = -1

# for ele in insertplace:
#     inputstr = inputstr[:ele[0]] + '(' + inputstr[ele[0]+1:]
#     inputstr = inputstr[]
# 비효율적

##############################

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

##############################
inputstr = sys.stdin.readline().rstrip().split('-')
# 55-50+40 이라면 ['55', '50+40']
sumsofsubstr = []
for ele in inputstr:
    sumofsubstr = 0
    substr = ele.split('+')
    #substr = ['55']
    for ele2 in substr:
        sumofsubstr += int(ele2)
    sumsofsubstr.append(sumofsubstr)
initnum = sumsofsubstr[0]
for i in range(1, len(sumsofsubstr)):
    initnum -= sumsofsubstr[i]
print(initnum)