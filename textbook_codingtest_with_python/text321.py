import sys


n = sys.stdin.readline().rstrip()
summary = 0

for i in range(0, len(n)//2):
    summary += int(n[i])

for i in range(len(n)//2, len(n)):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')