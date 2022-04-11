import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
line = [[False for _ in range(N + 1)] for _ in range(H + 1)]

for _ in range(M):
    a, b = tuple(map(int, input().split()))
    line[a][b] = True

candidates = [
    (i, j)
    for i in range(1, H + 1)
    for j in range(1, N)
    if not line[i][j]
]

min_count = 270


def is_impossible():
    if any([
        line[a][b] and line[a][b - 1]
        for a in range(1, H + 1)
        for b in range(2, N)
    ]):
        return False


def is_same_result():
    if is_impossible():
        return False

    current_result = [num for num in range(0, N + 1)]
    expected_result = [num for num in range(0, N + 1)]

    for a in range(1, H + 1):
        for b in range(1, N):
            if line[a][b]:
                current_result[b], current_result[b + 1] = current_result[b + 1], current_result[b]

    for i in range(1, N + 1):
        if current_result[i] != expected_result[i]:
            return False

    return True


def choose_width(current_idx, count):
    global min_count
    if count >= min_count:
        return

    if current_idx == len(candidates) or count == 3:
        return

    if is_same_result():
        min_count = min(count, min_count)

    choose_width(current_idx + 1, count)

    a, b = candidates[current_idx]
    line[a][b] = True
    choose_width(current_idx + 1, count + 1)
    line[a][b] = False


choose_width(0, 0)

if min_count > 3:
    print(-1)
else:
    print(min_count)

'''
5 5 6
1 1
3 2
2 3
5 1
5 4
'''
'''
5 8 6
1 1
2 2
3 3
4 4
3 1
4 2
5 3
6 4
'''
