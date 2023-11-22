a, b = input().split()
a = list(a)
b = list(b)

maxlen = max(len(a), len(b))
if len(a) < maxlen:
    for i in range(maxlen - len(a)):
        a.insert(0, '0')
if len(b) < maxlen:
    for i in range(maxlen - len(b)):
        b.insert(0, '0')

flatsum = []

for i in range(maxlen):
    flatsum.append(int(a[i]) + int(b[i]))
flatsum.insert(0, 0)

for i in range(maxlen, -1, -1):
    updigit = 0
    while flatsum[i] >= 10:
        flatsum[i] -= 10
        updigit += 1
    flatsum[i-1] += updigit

flatsum = list(map(str, flatsum))
result = ''.join(flatsum)
result = result.lstrip('0')
print(result)