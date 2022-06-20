MAX_INT = 4

N, M, H = tuple(map(int, input().split()))
pre_lines = [tuple(map(int, input().split())) for _ in range(M)]
total_lines = [[0] * (N + 1) for i in range(H + 1)]
for line in pre_lines:
    a, b = line
    total_lines[a][b] = 1


def idx_to_coordinate(current_idx):
    y, x = current_idx // (N - 1) + 1, current_idx % (N - 1) + 1
    return y, x


def is_all_itself():
    expected_result = [num for num in range(0, N)]
    result = [num for num in range(0, N)]
    for y in range(1, H + 1):
        for x in range(1, N + 1):
            if total_lines[y][x] == 1:
                result[x - 1], result[x] = result[x], result[x - 1]

    return result == expected_result


def is_continuous(y, x):
    return total_lines[y][x + 1] == 1 and total_lines[y][x - 1] == 1


def can_put(current_idx):
    y, x = idx_to_coordinate(current_idx)
    return total_lines[y][x] != 1 and not is_continuous(y, x)


def combination(current_idx, count):
    global answer, total_lines
    if count >= answer:
        return

    if is_all_itself():
        answer = min(answer, count)
        return

    if current_idx == (N - 1) * H:
        return

    y, x = idx_to_coordinate(current_idx)

    combination(current_idx + 1, count)

    if can_put(current_idx):
        total_lines[y][x] = 1
        combination(current_idx + 1, count + 1)
        total_lines[y][x] = 0


answer = MAX_INT
combination(0, 0)

if answer == MAX_INT:
    print(-1)
else:
    print(answer)

'''
2 0 3
'''
'''
2 1 3
1 1
'''
'''
5 5 6
1 1
3 2
2 3
5 1
5 4
'''
'''
6 5 6
1 1
3 2
1 3
2 5
5 5
'''
