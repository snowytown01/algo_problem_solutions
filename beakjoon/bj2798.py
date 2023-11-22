import sys


N, M = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
# candid = {}
candidlist = []

for a in array:
    for b in array:
        for c in array:
            if a + b + c <= M and a != b and a != c and b != c:
                # candid[a+b+c] = '{} {} {}'.format(a, b, c)
                candidlist.append(a+b+c)

# candidkey = list(candid.keys())
# candidkey.sort()
# popped = candidkey.pop()
# print(popped)

candidlist.sort()
print(candidlist.pop())

