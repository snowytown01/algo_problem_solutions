class solution():
    def makestar(self, iter):
        for i in range(1, iter+1):
            print(" " * (iter - i) + "*" * i)


iter = int(input())
obj = solution()
obj.makestar(iter)