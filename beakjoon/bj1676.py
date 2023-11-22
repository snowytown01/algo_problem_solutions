from math import factorial
import sys


n = int(sys.stdin.readline().rstrip())
result = 0

for x in str(factorial(n))[::-1]:
    if x != '0':
        break

    result += 1

print(result)