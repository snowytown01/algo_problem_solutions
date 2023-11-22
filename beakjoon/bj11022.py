class solution:
    def __init__(self, iter):
        self.iter = iter
    
    def calsum(self):
        for i in range(1, self.iter + 1):
            a, b = map(int, input().split())
            print("Case #" + str(i) + ": " + str(a) + " + " + str(b) + " = " + str(a + b))


iter = int(input())

obj = solution(iter)
obj.calsum()