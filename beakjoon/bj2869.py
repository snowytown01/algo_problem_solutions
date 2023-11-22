# A, B, V = map(int, input().split())

# V -= A
# count = 1

# count += V // (A-B)

# if V % (A-B) != 0: # 소수점이하가 남아있는경우
#     count += 1

# print(count)


A, B, V = map(int, input().split())

count = (V-B) // (A-B)

if (V-B) % (A-B) != 0:
    count += 1

print(count)

# A-B는 하루당 가는 net거리를 의미하고
# V-B는 맨마지막에 딱A만큼가고서 도착했을때를 대비해서 V에서 아래로 마중나가는것 net차원에서 계산하기위해

# 위의 풀이는 처음에 낮부터시작해서 A만큼가고서, 다음날 새벽에 B만큼 미끄러지고 낮에 A만큼가고
# 를 상정해서 만든 풀이