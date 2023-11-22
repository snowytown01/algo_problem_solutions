a = int(input())
b = int(input())
c = int(input())

mult = str(a * b * c)

print(mult.count("0"))
print(mult.count("1"))
print(mult.count("2"))
print(mult.count("3"))
print(mult.count("4"))
print(mult.count("5"))
print(mult.count("6"))
print(mult.count("7"))
print(mult.count("8"))
print(mult.count("9"))

# list, str 차이점: 
# list는 요소수정가능하고 다양한 형이 요소가될수있음, str음 요소수정불가능하고 오로지 str형만으로 이루어져있음