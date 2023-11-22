class solution:
    def __init__(self, lent, x):
        self.lent = lent
        self.x = x
    
    def print_small(self, list):
        for i in list:
            if i < self.x:
                print(i, end=' ')


lent, x = map(int, input().split())
list_inputed = list(map(int, input().split()))

obj = solution(lent, x)
obj.print_small(list_inputed)