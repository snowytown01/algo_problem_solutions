# inputed_str = input()
# count = 0

# if inputed_str[0] == ' ':
#     count -= 1

# if inputed_str[-1] == ' ':
#     count -= 1

# print(count + inputed_str.count(' ') + 1)


inputed_str = input().strip()

if inputed_str == "":
    print(0)
else:
    print(inputed_str.count(" ") + 1)

# 문자열.strip() 는 문자열 맨앞뒤에 인수로준 문자열을 구성하는 문자중에 하나라도 걸리는게 있으면 
# 거기서부터시작해서 문자열에 포함되지 않은 문자가 나올때까지 삭제해나간뒤 
# 포함되지 않은 문자에 부닥치면 거기서 종료
# 인자가 없으면 기본 ' ' 과 '\n' 의 조합
# (주의) 맨앞뒤에 인수문자가 없으면 strip적용안됨 중간문자 삭제불가능
# 잘라준결과를 사용하고싶다면 문자열 = 문자열.strip() 으로 재선언