class solution:
    def __init__(self):
        self.result = 0
    
    def adding(self, iter):
        for i in range(1, iter + 1):
            self.result += i
        return self.result

iter = int(input())

obj = solution()
print(obj.adding(iter))