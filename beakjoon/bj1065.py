def judge_num(num):
    result = 1 # 1 means yes
    the_d = 0

    stred_num = str(num)
    if len(stred_num) >= 2:
        the_d = int(stred_num[0]) - int(stred_num[1])
    
    for i in range(len(stred_num)-1):
        new_d = int(stred_num[i]) - int(stred_num[i+1])
        if new_d != the_d:
            result = 0 # 0 means no
            break
    
    return result


inputed_num = int(input())
count = 0

for i in range(1, inputed_num + 1):
    if judge_num(i) == 1:
        count += 1

print(count)


