import sys

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