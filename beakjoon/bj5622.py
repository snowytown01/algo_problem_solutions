def count_time(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0
    
    if alphabet[0:3].find(letter) != -1:
        result += 3
    elif alphabet[3:6].find(letter) != -1:
        result += 4   
    elif alphabet[6:9].find(letter) != -1:
        result += 5
    elif alphabet[9:12].find(letter) != -1:
        result += 6
    elif alphabet[12:15].find(letter) != -1:
        result += 7
    elif alphabet[15:19].find(letter) != -1:
        result += 8
    elif alphabet[19:22].find(letter) != -1:
        result += 9
    elif alphabet[22:26].find(letter) != -1:
        result += 10
    
    return result


def another(letter):
    word_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    result = 0  

    for i in word_list:
        if letter in i:
            result += word_list.index(i) + 3

    return result

def another2(letter):
    dial_list = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

    idx = ord(letter) - ord('A')
    
    return dial_list[idx] + 1

str = input()
result = 0
result2 = 0
result3 = 0

for i in str:
    result += count_time(i)
    result2 += another(i)
    result3 += another2(i)

print(result)
print(result2)
print(result3)