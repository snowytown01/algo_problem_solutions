#게임개발
import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# r, c, d = map(int, sys.stdin.readline().rstrip().split())
# map = []
# for i in range(n):
#     map.append(sys.stdin.readline().rstrip().split())


# def checkfour():
#     if (map[r-1][c] == '/' or map[r-1][c] == '1')\
#         and (map[r+1][c] == '/' or map[r+1][c] == '1')\
#         and (map[r][c-1] == '/' or map[r][c-1] == '1')\
#         and (map[r][c+1] == '/' or map[r][c+1] == '1'):
#         return True
#     else:
#         return False

# def checksea():
#     if d == 0 and map[r+1][c] == '1':
#         return True
#     if d == 1 and map[r][c-1] == '1':
#         return True 
#     if d == 2 and map[r-1][c] == '1':
#         return True
#     if d == 3 and map[r][c+1] == '1':
#         return True
#     return False

# result = 1
# map[r][c] = '/'
# while True:
#     if checkfour() == True:
#         if checksea() == True:
#             print(result)
#             break
#         else:
#             if d == 0: r+=1
#             if d == 1: c-=1
#             if d == 2: r-=1
#             if d == 3: c+=1
#     else:
#         d+=3
#         d%=4
#         if d==0 and map[r-1][c] == '0':
#             map[r-1][c] = '/'
#             result += 1
#             r-=1
#         if d==1 and map[r][c+1] == '0':
#             map[r][c+1] = '/'
#             result += 1
#             c+=1
#         if d==2 and map[r+1][c] == '0':
#             map[r+1][c] = '/'
#             result += 1
#             r+=1
#         if d==3 and map[r][c-1] == '0':
#             map[r][c-1] = '/'
#             result += 1
#             c-=1
    

####################################

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [[0]*m for _ in range(n)]
r, c, d = map(int, sys.stdin.readline(). rstrip().split())
visited[r][c] = 1

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

#북0, 서3, 남2, 동1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1: d = 3

fourcnt = 0
result = 1
while True:
    turn_left()
    nr = r + dr[d]
    nc = c + dc[d]
    if visited[nr][nc] == 0 and array[nr][nc] == 0:
        r = nr
        c = nc
        visited[r][c] = 1
        result += 1
        fourcnt = 0
    else:
        fourcnt += 1
    
    if fourcnt == 4:
        nr = r - dr[d]
        nc = c - dc[d]
        if array[nr][nc] == 0:
            r = nr
            c = nc
        else:
            break
        fourcnt = 0

    for ele in visited:
        print(ele)
    print()
    
print(result)