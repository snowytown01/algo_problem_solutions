import sys


array = [i for i in range(1, 31)]

# 특정값을 없앨때는 구체적인숫자가정해져서행동이강조되어서remove array.remove(값)
# 인덱스를 지정해서 그 인덱스의 값을 없앨때는 array.pop(인덱스) 혹은 del array[인덱스]

while True:
    try:
        n = int(input())
        array.remove(n)
    except:
        break

for i in array:
    print(i)



# 집합으로 만들어 차집합을 이용할수도 있음
# range(1, 31)은 range객체이다 이것을 리스트객체로 만들고싶다면 list(range(1, 31)) 집합객체로 만들고싶다면 set(range(1, 31))
# map함수는 iterator의 각요소에 함수를 적용하고난뒤 그것을 map객체로서 반환한다.

# uni = set(range(1, 31))
# inputed = set(map(int, sys.stdin))
# subst = uni - inputed
# print(min(subst))
# print(max(subst))