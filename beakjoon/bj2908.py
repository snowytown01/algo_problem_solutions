x, y = input().split()

a = "".join(reversed(x))
b = "".join(reversed(y))
c = x[::-1]
d = y[::-1]

# if int(a) >= int(b):
#     print(a)
# else:
#     print(b)

print(max(int(c), int(d)))

# if int(c) >= int(d):
#     print(c)
# else:
#     print(d)


# reversed는 문자열을 반대로한 오브젝트를 반환하고(리스트와비슷한형태)
# "구분자".join()은 구분자를 문자것이사이에 삽입하여 리스트를 문자열로 만들어주는 역할

# 문자열[처음:끝:공차] 은 슬라이스를 이용한것
# 처음인덱스이상 끝인덱스미만의 요소를 어떤공차순서로 뽑아낼지 정하는것
# 인덱스안적으면 양끝단으로 설정됨, 공차안적으면 1