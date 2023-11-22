import sys


def counting_sort(array):
    cnt_list = [0 for i in range(8001)]

    for i in range(len(array)):
        cnt_list[array[i]] += 1
    
    return cnt_list


def cal_mean(array):
    print(round(sum(array) / len(array)))

def cal_median(cnt_list, N):
    k = N // 2
    k += 1

    result = 0
    for i in range(-4000, 4001):
        while k != 0 and cnt_list[i] != 0:
            k -= 1
            cnt_list[i] -= 1
            result = i

    print(result)

def cal_freq(cnt_list):
    maximum = [cnt_list[0], 0] # 첫째는 맥시멈수, 둘째는 그인덱스
    before = 0
    for i in range(-4000, 4001):
        # i는 계수정렬리스트의 인덱스
        if cnt_list[i] > maximum[0]:
            maximum[0] = cnt_list[i]
            maximum[1] = i
            before = i
        elif cnt_list[i] == maximum[0]:
            maximum[1] = i
            before = maximum[1]       
    print(before)

def cal_range(array):
    print(max(array) - min(array))


N = int(input())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline().rstrip()))

cnted = counting_sort(array)
cnted2 = cnted.copy()

cal_mean(array)
cal_median(cnted, N)
cal_freq(cnted2)
cal_range(array)


# 함수밖의 array를 함수안에서 array[1] = 100 등을써서 수정해주면 함수밖에서도 유지가된다.