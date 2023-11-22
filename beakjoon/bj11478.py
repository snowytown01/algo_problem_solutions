import sys


s = sys.stdin.readline().rstrip()
result = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        result.add(temp)
    
print(len(result))