n = int(input())
s = []
result = []

count = 1
no_flag = True
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        result.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        result.append('-')
    else:
        no_flag = False


if no_flag == False: print('NO')
else:
    for i in result: print(i)