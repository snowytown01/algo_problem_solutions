class solution():
    def __init__(self, recur, in_str):
        self.recur = recur
        self.in_str = in_str
    
    def print_result(self):
        for i in range(len(self.in_str)):
            print(self.in_str[i] * self.recur, end = '')
        
        print("")

    def print_result_2(self):
        for i in self.in_str:
            print(i * self.recur, end = '')
        
        print()


case_num = int(input())

for i in range(case_num):
    recur, in_str = input().split()
    recur = int(recur)

    obj = solution(recur, in_str)
    obj.print_result_2()
