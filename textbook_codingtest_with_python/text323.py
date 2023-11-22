def solution(s):
    answer = len(s)
    length = len(s)
    for step in range(1, length//2+1):
        zipped = ""
        prev = s[0:step]
        count = 1
        for jump in range(step, length, step):
            if s[jump:jump+step] == prev:
                count += 1
            else:
                zipped += str(count)+prev if count != 1 else prev
                count = 1
                prev = s[jump:jump+step]
        zipped += str(count)+prev if count != 1 else prev
        answer = min(answer, len(zipped))
    print(answer)

s = 'aabbaccc' #2a2ba3c 7
solution(s)
