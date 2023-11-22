inputed = list(map(int, input().split()))
normal = [1, 1, 2, 2, 2, 8]

for i, j in zip(normal, inputed):
    print(i - j, end=' ')

# subst = [i - j for i, j in zip(normal, inputed)]
# print(subst)

# zip은 같은길이의 리스트 2개를 받은뒤 같은 인덱스끼리 짝을지어 튜플로하고 그런 튜플들이 모인 객체를만든다
# print할때 end='' 옵션을 추가해주면 기본으로 장착된\n을 다른것으로 바꿀수있다.
# print(*normal) 해주면 normal리스트안에 있는 요소 출력해줌