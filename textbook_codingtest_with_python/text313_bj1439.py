import sys


data = sys.stdin.readline().rstrip()

initnum = data[0]
change = 0
for i in range(1, len(data)):
    if data[i] != initnum:
        change += 1
        initnum = data[i]

if change % 2 == 0:
    print(change//2)
else:
    print(change//2 + 1)

##############################################
count0 = 0  #전부 0으로 바꾼다고 가정했을때 0으로 바꿀 1의 뭉치의 개
count1 = 0  #전부 1로 바꾼다고 가정했을때 1로 바꿀 0의 뭉치의 개수

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) -1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))

