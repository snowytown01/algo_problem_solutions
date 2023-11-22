import sys


n = int(sys.stdin.readline().rstrip())
data = sys.stdin.readline().rstrip().split()

current = [1, 1]

for ele in data:
    if current[0] == 1 and ele == 'U': continue
    elif current[1] == 1 and ele == 'L': continue
    elif current[0] == n and ele == 'D': continue
    elif current[1] == n and ele == 'R': continue
    else:
        if ele == 'U': current[0] -= 1
        elif ele == 'L': current[1] -= 1
        elif ele == 'D': current[0] += 1
        elif ele == 'R': current[1] += 1

print(current)

###############################
x, y = 1, 1
# LRUD순
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for ele in data:
    for i in range(4):
        if ele == move_type[i]:
            newx = x + dx[i]
            newy = y + dy[i]
    if newx<1 or newy<1 or newx>n or newy>n:
        continue
    x, y = newx, newy

print(x, y)