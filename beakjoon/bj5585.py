import sys


money = 1000 - int(sys.stdin.readline().rstrip())

sortofcoins = [500, 100, 50, 10, 5, 1]

#현재상태에서 가장좋은 500으로 먼저 깎을만큼 깎기를 모든 돈종류에 대해서 반복하면, 결국 최선이됨 왜냐면 모든 값이 앞값의 약수이기때문
result = 0
for ele in sortofcoins:
    result += money//ele
    money %= ele

print(result)
