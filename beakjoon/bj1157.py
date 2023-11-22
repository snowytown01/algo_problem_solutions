# alphabet_min = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# count_result = []


# inputed_str = input()

# for i in alphabet_min:
#     count_result.append(inputed_str.count(i))

# for j in range(len(alphabet_maj)):    
#     count_result[j] += inputed_str.count(alphabet_maj[j])


# maximum = max(count_result)
# if count_result.count(maximum) != 1:
#     print("?")
# else:
#     maximum_index = count_result.index(maximum)
#     print(alphabet_maj[maximum_index])



inputed_str = input().upper()
n = 0

for i in map(chr, range(65, 91)):
    counted = inputed_str.count(i)

    if n < counted:
        n = counted
        maxalpha = i

    elif n == counted:
        maxalpha = '?'

print(maxalpha)