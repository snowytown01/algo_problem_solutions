num = input()
array = []

for i in num:
    array.append(int(i))

array.sort(reverse=True)
result = ''.join(str(ele) for ele in array)

print(result)
