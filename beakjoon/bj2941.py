# alphabet = 'abcdefghijklmnopqrstuvwxyz'
c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# letter = input()
# result = 0  

# for i in c_alphabet:
#     result += letter.count(i)
#     letter = letter.replace(i, '|')

# for i in alphabet:
#     result += letter.count(i)

# print(result)

letter = input()
    
for i in c_alphabet:
    letter = letter.replace(i, '*')

print(len(letter))


# replace는 문자열내의 모든 문자를 리플레이스함 이를 사용해 strip에서는 못했던 중간문자 삭제가 가능해짐
# replace한것을 유지하려면 문자열변수를 재초기화하면됨
