# #   0123456789012
# # 0 WBBBBBBBWBWBW
# # 1 BBBBBBBBBWBWB
# # 2 WBBBBBBBWBWBW
# # 3 BBBBBBBBBWBWB
# # 4 WBBBBBBBWBWBW
# # 5 BBBBBBBBBWBWB
# # 6 BBBBBBBBWBWBW
# # 7 BBBBBBBBBWBWB
# # 8 WWWWWWWWWWBWB
# # 9 WWWWWWWWWWBWB

# 기본 아이디어: 
# 왼쪽위부터 가로길이 8 세로길이 8의 temp판을 잡고
# 그것을 체스판으로 만들기위해 얼마나 칠해야하는지 기록용리스트에 어팬드한다
# 위 2과정을 전체판의 끝에 달할때까지 반복
# 기록용리스트에서 min값을 출력

# step2상세:
# 리스트를 받아와서
# 왼쪽위가 B일때 얼마나 칠해야하는지 확인하고 W일때 얼마나 칠해야하는지 확인한뒤
# (행열의 인덱스를 더했을때 짝수이면 왼위부터 전체 왔다갔다, 홀수이면 그다음글자의 왔다갔다)
# 둘중에서 최소값을 출력하는 함수를 만든다.
# 그 값을 기록용 리스트에 어팬드

import sys

N, M = map(int, sys.stdin.readline().rstrip().split()) # N,M은 인덱스가아니고 길이다
plate = []
for _ in range(N): plate.append(sys.stdin.readline().rstrip())

def makechess(i, j):
    chess = []
    temp = ''
    for row in range(i, i+8):
        for col in range(j, j+8):
            temp += plate[row][col]
        chess.append(temp)
        temp = ''
    return chess

def calcoloring(chess):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and chess[i][j] != 'B': count1 += 1   # 왼위글자가 B일때
            if (i+j) % 2 != 0 and chess[i][j] != 'W': count1 += 1

            if (i+j) % 2 == 0 and chess[i][j] != 'W': count2 += 1  # 왼위글자가 W일때
            if (i+j) % 2 != 0 and chess[i][j] != 'B': count2 += 1 
            #주의, %는 */등과같은 우선순위이다 앞에 (i+j)괄호 필수
    return min(count1, count2)

record = []
for i in range(N-7):
    for j in range(M-7): # 이 ij는 체스판의 맨왼위가될 전체판의 인덱스이다.
        chess = makechess(i, j) # i,j를 기반으로 체스를 떼올 함수
        record.append(calcoloring(chess))

print(min(record))




# j+1 != M and chess[i][j] != chess[i][j+1]:
# 처럼 j+1이 주어진 chess리스트의 범위를 넘어설 위험이있으면
# j+1 != M 이라는 방지용 코드를 앞에 먼저 써준다
# 왜냐하면 파이썬은 인터프리터 언어니까