N = int(input())
causes = []

def add_digit(strnum):
    result = 0
    for i in strnum:
        result += int(i)

    return result


for i in range(1, N):
    temp = i + add_digit(str(i))
    if  temp == N:
        causes.append(i)
        break

if len(causes) == 0:
    print(0)
else:
    print(min(causes))

# 최소만 구하면되니까 if문에서 break해도됨