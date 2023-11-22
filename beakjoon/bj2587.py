import sys


array = []

for line in sys.stdin:
    line = int(line.rstrip())
    array.append(line)

sorted = sorted(array)
medium_idx = len(sorted)//2

print(sum(array)//len(array))
print(sorted[medium_idx])



# 입력수가 주어지지 않을때 끝까지 읽어들이는법
# 첫번째
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break

# 두번째
# import sys
# for line in sys.stdin:
#     a, b = map(int, line.split())
#     print(a + b)

# sys.stdin 은 버퍼그자체(buffer(aa\nbb\ncc\n))를 담은 객체이다.
# f = open('filename.txt', 'wb') 에서 f는 파일의텍스트를 버퍼로 담은 객체이다.
# ㄴ첫번째인자는 파일이름이다. 열려는파일이같은폴더내의파일이면경로생략가능
# ㄴ두번째인자는 해당파일을 어떤모드로 읽을지 결정하는것. rwa tb 종류가있음
# ㄴ만약 앞글자가 비어있다면 기본r모드, 뒷글자가 비어있다면 기본t모드, 둘다비었으면 그냥 두번째인자생략가능

# 위 2가지 버퍼객체를 담는 변수는 기본적으로 \n기준으로 iterable하다 따라서 그자체로 for문이나 map등에 리스트같이 사용가능
# 이때 버퍼객체안은 ~\n~\n~\n 상태인데 각 ~\n 을 str로서 받아들인다.
# sys.stdin.readline()은 버퍼에서처음나오는\n까지만 가져와서 str화한것
# sys.stdin.readlines()는 버퍼에서\n의오른쪽을 구분선으로 잘라서 list화한것
# f.readline() f.readlines() 도 같음