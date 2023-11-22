import sys


# def counting_sort(array):
#     cnt_list = [0 for i in range(10001)]

#     for i in range(len(array)):
#         cnt_list[array[i]] += 1

#     for i in range(len(cnt_list)):
#         for j in range(cnt_list[i]):
#             print(i)

# n = int(input())
# array = []
# for i in range(n):
#     array.append(int(sys.stdin.readline().rstrip()))

# counting_sort(array)

# 위의 방법은 append때문에 메모리 초과가 나기때문에 입력받은 즉시 해당 숫자의 인덱스를 증가
n = int(input())
cnt_list = [0 for i in range(10001)]

for i in range(n):
    temp = int(sys.stdin.readline().rstrip())
    cnt_list[temp] += 1

for i in range(len(cnt_list)): #전체 인덱스 순회용 i
    for j in range(cnt_list[i]): #숫자 반복출력용 j
        print(i)