a = int(input())
b = int(input())
pnum_list = []

for i in range(a, b+1):
    if i == 1:
        pass
    elif i == 2:
        pnum_list.append(i)
    else:
        pnum_list.append(i)
        for j in range(2, i):
            if i % j == 0:
                pnum_list.pop()
                break


if len(pnum_list) == 0:
    print(-1)
else:
    print(sum(pnum_list))
    print(pnum_list[0])
