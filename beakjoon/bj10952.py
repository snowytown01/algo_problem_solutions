class solution:
    def calsum(self):
        while True:
            a, b = map(int, input().split())
            if a == 0 and b == 0:
                break
            else:
                print(a + b)


obj = solution()
obj.calsum()