import sys


def make_starmap(iter):
    if iter == 1:
        return ['*']
    
    previous = make_starmap(iter//3)
    nowresult = []

    for i in previous:
        nowresult.append(i*3)
    for i in previous:
        nowresult.append(i+' '*(iter//3)+i)
    for i in previous:
        nowresult.append(i*3)
    
    return nowresult
    

N = int(sys.stdin.readline().rstrip())

print('\n'.join(make_starmap(N)))

# 재귀를 풀땐 a_n이 이미 알려져있다고 가정한뒤 
# 그것을 '이용해' a_(n+1)의 결과를 내려고 접근해야한다

# a_(n+1) = a_n a_n a_n
#           a_n     a_n
#           a_n a_n a_n 
# 인데, print의 구조상 한번출력된것 뒤에 a_n을 붙이는 식으로 하긴 어려우므로
# 완벽히 한줄을 만든다음에 다음줄로 넘어가야하는 식으로 속으로 들어가야함

# a_n을 한줄씩 리스트에 담고 a_(n+1)에서 a_n의요소를 하나씩(즉,한줄씩) 가져와 a_(n+1)의 결과치로 만들어서
# a_n을 이용한 a_(n+1)의 달성이 가능해짐 이렇게 a_n의 속까지 들어가서 a_(n+1)의 결과치를 만들게된건 다 print의 한계때문
