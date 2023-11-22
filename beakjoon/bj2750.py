# 삽입정렬이용
def insert_sort(inputed_list):
    for i in range(1, len(inputed_list)):
        for j in range(i, 0, -1):
            if inputed_list[j] < inputed_list[j-1]:
                inputed_list[j], inputed_list[j-1] = inputed_list[j-1], inputed_list[j]
            else:
                break            
    return inputed_list

numcnt = int(input())
inputed_list = []
for i in range(numcnt):
    a = int(input())
    inputed_list.append(a)

result = insert_sort(inputed_list)
for i in result:
    print(i)




# 버선삽(버선으로 삽을퍼서 구시대적 O(n^2), 버선삽순으로 효율적)
# 퀵힙합(빠른 힙합이라서 신시대적 O(nlogn), 퀵힙합순으로 효율적)
# 계수정렬(가장 빠름 O(n+k))