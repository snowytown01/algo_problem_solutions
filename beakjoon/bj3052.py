nlist = []

for i in range(10):
    nlist.append(int(input()) % 42)

setted = set(nlist)
print(len(setted))

# inputed_str = input()
# for i in range(len(inputed_str)):
#     print(inputed_str[i])

# setted_str = set(inputed_str)
# print(setted_str)

# set은 str 문자열에서도 동일하게 문자단위로 중복되는 문자를 제거한뒤 문자단위로 윈소를 취한다.