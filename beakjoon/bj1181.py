import sys


# N = int(sys.stdin.readline().rstrip())
# array = []
# temparray = []
# lenarray = []

# for i in range(N):
#     inpstr = sys.stdin.readline().rstrip()
#     array.append(inpstr)
# array = list(set(array))

# while(len(array) != 0):
#     lenarray = list(map(len, array))
#     targetlen = min(lenarray)
    
#     for i in array:
#         if len(i) == targetlen:
#             temparray.append(i)

#     array = list(set(array) - set(temparray))

#     temparray.sort()
#     for i in temparray:
#         print(i)
#     temparray.clear()
#     lenarray.clear()

N = int(sys.stdin.readline().rstrip())
wordset = set()

for i in range(N):
    wordset.add(sys.stdin.readline().rstrip())

wordset = list(wordset)
wordset.sort() # abcd순으로
wordset.sort(key=lambda x: len(x)) # 그후 길이순으로

for i in wordset:
    print(i)

# 절대 for i in array에서 array의 요소를 for문안에서 변형하지말것
# 변형결과가 그대로 다음번째 요소에대해 실행할 판이됨

# sort(key=함수명) 이란, sort할 리스트의요소를 해당함수의 x에넣어서 각각적용시킨 결과값을 기준으로 리스트의요소를 오름차순으로 정렬한다는뜻
# lambda x: len(x) 이란, 함수정의의 간략화버전으로 x가 매개변수, len(x)가 리턴값이다. 일회용함수다.
# 이를조합해 sort(key=lambda x: len(x)) 등으로 사용가능
# 길이라는기준에따라 나눴을때 같은 길이라면 기존순서를 유지하고, 다르다면 바꾸는것

# set을 만들때는 wordset = set() 이다 리스트처럼 []만쓰면되는게 아님