#위치가 주어졌을때 옮길수 있는 가지수를 구하라
import sys


data = sys.stdin.readline().rstrip()
coord = []

changestr = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(9):
    if changestr[i] == data[0]: coord.append(i)
coord.append(int(data[1]))

eda = [-2, 2]
ude = [-1, 1]

result = []
for e in eda:
    for u in ude:
        #vh
        temp1 = coord.copy()
        temp1[1] += e
        temp1[0] += u
        result.append(temp1)

        #hv
        temp2 = coord.copy()
        temp2[0] += e
        temp2[1] += u
        result.append(temp2)

cnt = 0
for ele in result:
    if 1 <= ele[0] <= 8 and 1 <= ele[1] <= 8:
        cnt += 1

print(cnt)

#######################################

row = int(data[1])
column = ord(data[0]) - ord('a') + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
