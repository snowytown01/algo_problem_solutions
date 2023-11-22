import sys


n = int(sys.stdin.readline().rstrip())

for i in range(n):
    stack = []

    somestring = sys.stdin.readline().rstrip()
    for s in somestring:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")