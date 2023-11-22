# 퀵정렬로 풀고자 했지만 시간초과 -> .sort() 내장함수사용
# 또한 input()을 썼더니 시간초과 -> sys.stdin.readline().rstrip() 사용
import sys


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

n = int(sys.stdin.readline().rstrip())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

# quick_sort(array, 0, len(array)-1)
array.sort()

for i in array:
    print(i)