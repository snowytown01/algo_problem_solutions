import sys

def counting_sort(array, k):
    cnt_list = [0 for i in range(10001)]
    result = 0

    for i in range(len(array)):
        cnt_list[array[i]] += 1
    
    for i in range(len(cnt_list)-1, -1, -1):
        while cnt_list[i] != 0 and k != 0:
            result = i
            k -= 1
            cnt_list[i] -= 1
    
    print(result)



N, k = map(int, sys.stdin.readline().rstrip().split())
scores = list(map(int, sys.stdin.readline().rstrip().split()))

counting_sort(scores, k)