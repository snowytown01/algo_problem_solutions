# string = input()

# result = [-1 for i in range(26)]

# for i in range(len(string)):
#     if result[ord(string[i]) - 97] == -1:
#         result[ord(string[i]) - 97] = i

# for i in range(26):
#     print(result[i], end=" ")


string = input()
alpha_list = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha_list:
    print(string.find(i), end = ' ')