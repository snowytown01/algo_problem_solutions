class solution():
    def __init__(self, inputed_list):
        self.inputed_list = inputed_list
        
    def cal_percent(self):
        mean = sum(self.inputed_list) / len(self.inputed_list)
        result = 0

        for i in self.inputed_list:
            if i > mean:
                result += 1

        print(format(result / len(inputed_list) * 100, ".3f") + "%")


line = int(input())

for i in range(line):
    inputed_list = list(map(int, input().split()))
    inputed_list.pop(0)

    obj = solution(inputed_list)
    obj.cal_percent()

# split은 자르고난 문자열로 구성된 리스트를반환
# map은 각 문자열을 int로 맵핑한 객체를반환
# list는 map객체를 리스트로반환

# data = input().split()
# print(data)
# print(type(data))

# data2 = map(int, input().split())
# print(data2)
# print(type(data2))

# data3 = list(map(int, input().split()))
# print(data3)
# print(type(data3))