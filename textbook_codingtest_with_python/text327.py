n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] #맵
info = []

#맵에 과일 넣기
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

#회전정보저장
l = int(input())
for _ in range(l):
    x, c = input().split() #x는 초, c는 회전방식
    info.append((int(x), c))

#0인덱스를 처음으로 x를 수직좌표로 y를 수평좌표로 본것
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    x, y = 1, 1 #뱀의 머리위치를 1,1로 알기쉽게
    data[x][y] = 2 #뱀이 차지하는 좌표엔 2로 표시
    direction = 0 #처음에는 동쪽
    time = 0 #경과시간
    index = 0 #회전정보
    q = [(x, y)] #각 순간의 뱀의 몸통의 정보를 저장 0인덱스가 꼬리쪽
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())