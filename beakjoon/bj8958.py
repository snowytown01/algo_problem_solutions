class solution():
    def __init__(self, str):
        self.str = str
    
    def cal_score(self):
        bucket = 0
        result = []
        
        for i in range(len(self.str)):
            if self.str[i] == 'O':
                bucket += 1
                result.append(bucket)

            else:
                bucket = 0
        
        print(sum(result))

class solution2():
    def __init__(self, str):
        self.str = str

    def cal_score(self):
        bucket = 1
        result = 0

        for i in range(len(self.str)):
            if self.str[i] == 'O':
                result += bucket
                bucket += 1
            
            else:
                bucket = 1
        
        print(result)


line = int(input())
for i in range(line):
    obj = solution2(input())
    obj.cal_score()

