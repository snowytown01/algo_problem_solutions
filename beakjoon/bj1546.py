class solution:
    def __init__(self, count, i_list):
        self.count = count
        self.i_list = i_list
    
    def cal_new_exp(self):
        max_num = max(self.i_list)

        for index in range(self.count):
            self.i_list[index] = self.i_list[index]/max_num * 100
        
        result = (sum(self.i_list)) / self.count
        print(result)


count = int(input())
i_list = list(map(int, input().split()))

obj = solution(count, i_list)
obj.cal_new_exp()
