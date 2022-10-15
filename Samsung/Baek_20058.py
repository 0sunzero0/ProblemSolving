from collections import deque


def init():
    N, Q = tuple(map(int, input().split()))
    ice = [list(map(int, input().split())) for _ in range(2 ** N)]
    levels = list(map(int, input().split()))
    return N, Q, ice, levels


def rotate_grid_90_degree_clockwise(start_r, start_c, box_size):
    for i in range(box_size):
        for j in range(box_size):
            next_grid[start_r + i][start_c + j] = grid[start_r + box_size - 1 - j][start_c + i]


def rotate(level):
    for r in range(grid_size):
        for c in range(grid_size):
            next_grid[r][c] = 0

    box_size = 2 ** level

    for r in range(0, grid_size, box_size):
        for c in range(0, grid_size, box_size):
            rotate_grid_90_degree_clockwise(r, c, box_size)

    for r in range(grid_size):
        for c in range(grid_size):
            grid[r][c] = next_grid[r][c]


def in_range(r, c):
    return 0 <= r < grid_size and 0 <= c < grid_size


def is_ice(r, c):
    return grid[r][c] > 0


def melt():
    for r in range(grid_size):
        for c in range(grid_size):
            next_grid[r][c] = 0

    for r in range(grid_size):
        for c in range(grid_size):
            count = 0
            for dr, dc in zip(drs, dcs):
                next_r, next_c = r + dr, c + dc
                if in_range(next_r, next_c) and is_ice(next_r, next_c):
                    count += 1
            if count < 3 and is_ice(r, c):
                next_grid[r][c] -= 1

    for r in range(grid_size):
        for c in range(grid_size):
            grid[r][c] += next_grid[r][c]


def get_total_ice():
    result = 0
    for r in range(grid_size):
        for c in range(grid_size):
            result += grid[r][c]
    return result


def bfs(start_r, start_c):
    bfs_queue = deque()
    count = 0

    bfs_visit[start_r][start_c] = True
    bfs_queue.append((start_r, start_c))
    count += 1

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()
        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c):
                if not bfs_visit[next_r][next_c] and is_ice(next_r, next_c):
                    bfs_visit[next_r][next_c] = True
                    bfs_queue.append((next_r, next_c))
                    count += 1

    return count


def get_max_area():
    result = 0
    for r in range(grid_size):
        for c in range(grid_size):
            if is_ice(r, c):
                result = max(result, bfs(r, c))
    return result


def print_grid():
    for r in range(grid_size):
        for c in range(grid_size):
            print(grid[r][c], end=" ")
        print()


N, Q, grid, levels = init()
grid_size = 2 ** N
next_grid = [
    [0 for _ in range(grid_size)]
    for _ in range(grid_size)
]

# 오른쪽, 아래, 왼쪽, 위
drs, dcs = [0, 1, -1, 0], [1, 0, 0, -1]

for level in levels:
    if level != 0:
        rotate(level)
        # print_grid()
    melt()

bfs_visit = [[False] * grid_size for _ in range(grid_size)]

print(get_total_ice())
print(get_max_area())

'''
3 1
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32
33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48
49 50 51 52 53 54 55 56
57 58 59 60 61 62 63 64
1
'''
'''
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
'''
'''
3 5
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 0 3 2
'''
