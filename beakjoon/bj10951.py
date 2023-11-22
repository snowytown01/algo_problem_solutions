class solution:
    def calsum(self):
        while True:
            try:
                a, b = map(int, input().split())
                print(a + b)
            except:
                break

obj = solution()
obj.calsum()