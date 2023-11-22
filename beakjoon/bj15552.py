import sys


class solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calsum(self):
        print(self.a + self.b)


linecount = int(sys.stdin.readline().rstrip())
# linecount = int(input())

for i in range(linecount):
    line = sys.stdin.readline().strip()
    # line = input()
    a, b = map(int, line.split())

    obj = solution(a, b)
    obj.calsum()