MAX_VALUE = (50 + 50) * 13

N, M = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

chicken_pos = []
city_pos = []
selected_chicken_pos = []
min_total_dist = MAX_VALUE
temp_grid = [
        [0] * N for _ in range(N)
]


for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            chicken_pos.append((i, j))
        elif grid[i][j] == 1:
            city_pos.append((i, j))


def is_chicken_pos(y, x):
    global temp_grid
    return temp_grid[y][x] == 2


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def get_dist():
    global selected_chicken_pos, city_pos
    result = 0

    for pos1 in city_pos:
        min_dist = MAX_VALUE
        y1, x1 = pos1
        for pos2 in selected_chicken_pos:
            y2, x2 = pos2
            min_dist = min(min_dist, abs(y1 - y2) + abs(x1 - x2))

        result += min_dist

    return result


def combination(curr_idx):
    global min_total_dist

    if curr_idx == len(chicken_pos):
        if len(selected_chicken_pos) == M:
            min_total_dist = min(min_total_dist, get_dist())
        return

    selected_chicken_pos.append(chicken_pos[curr_idx])
    combination(curr_idx + 1)
    selected_chicken_pos.pop()
    combination(curr_idx + 1)


combination(0)
print(min_total_dist)

'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''
'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''
