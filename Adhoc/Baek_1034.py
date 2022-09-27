N, M = tuple(map(int, input().split()))
lamps = [list(input()) for _ in range(N)]
K = int(input())

lamp_off_cnt = [0] * N
for row in range(N):
    off_cnt = 0
    for col in range(M):
        if lamps[row][col] == '0':
            off_cnt += 1
    lamp_off_cnt[row] = off_cnt


def get_same_row_cnt(row):
    result = 0
    for another_row in range(N):
        if another_row != row and lamps[another_row] == lamps[row]:
            result += 1
    return result


answer = 0
for row in range(N):
    if lamp_off_cnt[row] <= K and lamp_off_cnt[row] % 2 == K % 2:
        answer = max(answer, 1 + get_same_row_cnt(row))

print(answer)

'''
3 2
01
10
10
1
'''
