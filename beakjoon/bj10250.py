line = int(input())

for i in range(line):
    row, col, N = map(int, input().split())

    if N % row != 0:
        allocate_col = N // row + 1
        allocate_row = N % row
    else:
        allocate_col = N // row
        allocate_row = row

    print(str(allocate_row) + str(allocate_col).zfill(2))


# 문자열.zfill(총문자열길이) 라고하면 총문자열길이에 맞춰서 문자열앞에 0을 추가해줌
# 나머지%를 사용할때는 반드시 나머지가 0이되는 때를 주의할것

# if else문을 안쓰고 N을 N-1로 해서 맨아래층에서 나머지가 0이되도록 늦출수도있음
    allocate_col = (N-1) // row + 1
    allocate_row = (N-1) % row + 1

    print(str(allocate_row) + str(allocate_col).zfill(2))