class solution():
    def makestar(self, iter):
        for i in range(1, iter+1):
            print("*" * i)


iter = int(input())
obj = solution()
obj.makestar(iter)