def d(num):
    result = 0
    stred_num = str(num)
    result += num
    
    for i in stred_num:
        result += int(i)
    
    return result
        

def find_selfnum(allnumlist):
    for i in range(1, 10001):
        try:
            allnumlist.remove(d(i))
        except ValueError:
            pass
    
    return allnumlist

allnumlist = list(range(1, 10001))
resultlist = find_selfnum(allnumlist)

for i in resultlist:
    print(i)


# 없애고자 하는 자릿수n으로 num % 10^n 하면 없애고자하는 자리수 아래것이 남음
# 가지고자 하는 자릿수n으로 num // 10^n 하면 구하고자하는 자리수가 나옴