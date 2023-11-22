class solution:
    def __init__(self, totalprice):
        self.result = 0
        self.total = totalprice
    
    def calsum(self, iter):
        for i in range(iter):
            price, count = map(int, input().split())
            self.result += price * count

    def compare(self):
        if self.result == self.total:
            print("Yes")
        else:
            print("No")

totalprice = int(input())
iter = int(input())

obj = solution(totalprice)

obj.calsum(iter)
obj.compare()