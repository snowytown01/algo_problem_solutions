nlist = []

for i in range(9):
    nlist.append(int(input()))

maxnum = max(nlist)
print(maxnum)
print(nlist.index(maxnum)+1)

# tmp = 0
# tmp_index = 0
# for i in range(9):
#     inputed = int(input())
#     if tmp <= inputed:
#         tmp = inputed
#         tmp_index = i+1

# print(tmp)
# print(tmp_index)
