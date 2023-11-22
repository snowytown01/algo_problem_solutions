import sys

num = 0
cnt = 0
inputcnt = int(sys.stdin.readline().rstrip())

while cnt != inputcnt:
    num += 1
    if '666' in str(num):
        cnt += 1

print(num)