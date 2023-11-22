import sys


N = int(sys.stdin.readline().rstrip())
inplist = []
inpdict = {}

# for i in range(N):
#     inpdict[sys.stdin.readline().rstrip()] = i
# print(inpdict)

# keys = list(inpdict.keys())
# keys.sort()
# print(keys)

# keys.sort(key=lambda x: inpdict.get(x))

# print(keys)

for i in range(N):
    inplist.append(list(sys.stdin.readline().rstrip().split()))


inplist.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(inplist[i][0], inplist[i][1])

# 주의, 문자열형태로된 숫자를 sort하면 전체수의 대소에 관계없이 맨앞자리부터 비교해나감
# 그래서 123이 15 보다 작은수로 인식됨(1까진같고 2,5를 비교시에 2가더작으니까)
# 1 11 111 을 비교시엔 맨앞이같으니패스, 두번째에서 1은 두번째가없으니 제일작은걸로 취급
# 그리고 11 111은 두번째가같으니 패스, 세번째에서 11은 세번째가없으니 그다음작은걸로 취급