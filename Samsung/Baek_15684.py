MAX_INT = 4
N, M, H = tuple(map(int, input().split()))
pre_lines = [tuple(map(int, input().split())) for _ in range(M)]
total_lines = [[0] * (N + 1) for _ in range(H + 1)]
for line in pre_lines:
    a, b = line
    total_lines[a][b] = 1


def is_all_itself():
    for x in range(1, N + 1):
        current_x = x
        for y in range(1, H + 1):
            if total_lines[y][current_x - 1] == 1:
                current_x -= 1
            elif total_lines[y][current_x] == 1:
                current_x += 1

        if current_x != x:
            return False

    return True


def is_continuous(y, x):
    return total_lines[y][x + 1] == 1 or total_lines[y][x - 1] == 1


def combination(current_idx, count):
    global answer, total_lines
    if count >= answer or count > M:
        return

    if is_all_itself():
        answer = min(answer, count)
        return

    for candidate_idx in range(current_idx, len(candidate)):
        y, x = candidate[candidate_idx]
        if not is_continuous(y, x):
            total_lines[y][x] = 1
            combination(candidate_idx + 1, count + 1)
            total_lines[y][x] = 0


candidate = []
for i in range(1, H + 1):
    for j in range(1, N):
        if not is_continuous(i, j) and not total_lines[i][j]:
            candidate.append((i, j))


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
