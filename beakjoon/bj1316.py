# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# record = []
# result = 0

# def group(letter):
#     while len(letter) > 0:
#         record.append(letter[0])
#         letter = letter.lstrip(letter[0])

# num = input()

# for i in range(int(num)):
#     letter = input()
#     group(letter)
    
#     result += 1
#     for i in alphabet:
#         if record.count(i) > 1:
#             result -= 1
#             break
    
#     record = []

# print(result)

#/////////////////////
# num = int(input())
# result = 0

# for i in range(num):
#     letter = input()
#     changing_point = 0

#     for i in range(len(letter) - 1):
#         if letter[i] != letter[i+1]:
#             changing_point += 1
    
#     if changing_point == len(set(letter))-1:
#         result += 1

# print(result)


num = int(input())
result = 0

for i in range(num):
    letter = input()

    if list(letter) == sorted(letter, key = letter.find):
        result += 1

print(result)
    

# 전역변수는 이 에디터전체에 적용되는 변수로 맨앞에 띄어쓰기없이 바로 정의된 변수를 의미한다.
# 지역변수는 def안에 정의된 변수를 의미한다.
# def안에서 전역변수를 사용할땐 따로 명시를 안해도되나, def안에서 전역변수를 수정하고자할때는 global a 라고 선언후
# a = ~~ 라고 해주면 된다.

# sorted함수는 첫번째인자에서 크기가 작은것부터 순서대로 정렬한뒤 정렬된것을 리스트로 반환한다.
# 만일 첫번째인자내의 원소들이 서로 이질적인것이라면 두번째인자로 key=함수명 을 사용할수있다
# 각 원소에 인자로준 함수를 각각 적용한결과가 작은것부터 원본원소를 정렬시킨다.