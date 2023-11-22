cache = {1: 0, 2: 1, 3: 1, 4: 2}

def count_minium_of(num):
    if num in cache:
        return cache[num]

    cnt = min(count_minium_of(num//5) + num%5 ,count_minium_of(num//3) + num%3, count_minium_of(num//2) + num%2) + 1
    cache[num] = cnt
    return cnt




num = int(input())
result = count_minium_of(num)

print(cache)
print(result)