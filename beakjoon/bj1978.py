N = int(input())
num_list = list(map(int, input().split()))
result = len(num_list)

for i in num_list:
    if i == 1:
        result -= 1
    elif i == 2:
        pass
    else:
        for k in range(2, i):
            if i % k == 0:
                result -= 1
                break

print(result)
