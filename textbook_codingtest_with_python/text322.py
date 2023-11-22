import sys


data = sys.stdin.readline().rstrip()
result = []
value = 0

for ele in data:
    if ele.isalpha():
        result.append(ele)
    else:
        value += int(ele)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
