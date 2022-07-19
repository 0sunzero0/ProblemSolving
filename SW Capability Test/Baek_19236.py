def init():
    grid = [[(0, 0) for _ in range(N)] for _ in range(N)]

    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            grid[r][c] = (row[c * 2], row[c * 2 + 1] - 1)

    return grid


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def fish_can_go(r, c):
    return in_range(r, c) and grid[r][c] != SHARK


def get_next(y, x, curr_dir):
    for next_idx in range(DIR_NUM):
        next_dir = (curr_dir + next_idx) % DIR_NUM
        ny, nx = y + dys[next_dir], x + dxs[next_dir]
        if fish_can_go(ny, nx):
            return (ny, nx, next_dir)

    return (y, x, curr_dir)


def swap(r, c, nr, nc):
    grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]


def move_fish(target_num):
    for y in range(N):
        for x in range(N):
            fish_num, curr_dir = grid[y][x]
            if fish_num == target_num:
                ny, nx, next_dir = get_next(y, x, curr_dir)
                grid[y][x] = (fish_num, next_dir)
                swap(y, x, ny, nx)
                return


def move_all_fish():
    for target_num in range(1, N * N + 1):
        move_fish(target_num)


def shark_can_go(r, c):
    return in_range(r, c) and grid[r][c] != BLANK


def is_complete(cy, cx, cdir):
    for step in range(1, N + 1):
        ny, nx = cy + dys[cdir] * step, cx + dxs[cdir] * step
        if shark_can_go(ny, nx):
            return False
    return True


def get_max_fish_sum(cy, cx, cdir, fish_sum):
    global answer

    if is_complete(cy, cx, cdir):
        answer = max(answer, fish_sum)
        return

    for step in range(1, N + 1):
        ny, nx = cy + dys[cdir] * step, cx + dxs[cdir] * step
        if shark_can_go(ny, nx):
            temp_grid = [
                [grid[i][j] for j in range(N)]
                for i in range(N)
            ]

            # 물고기 잡아먹음
            extra_fish_sum, ndir = grid[ny][nx]
            grid[cy][cx], grid[ny][nx] = BLANK, SHARK

            # 물고기 이동
            move_all_fish()

            # 다음 탐색 진행
            get_max_fish_sum(ny, nx, ndir, fish_sum + extra_fish_sum)

            # 원래대로
            for i in range(N):
                for j in range(N):
                    grid[i][j] = temp_grid[i][j]


answer = 0

N = 4
DIR_NUM = 8

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, -1, -1, -1, 0, 1, 1, 1]

BLANK = (0, 0)
SHARK = (-1, -1)
grid = init()

# 초기 상어가 잡아먹음
init_fish_sum, init_dir = grid[0][0]
grid[0][0] = SHARK

# 물고기 이동
move_all_fish()

# 백트레킹
get_max_fish_sum(0, 0, init_dir, init_fish_sum)
print(answer)

'''
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
'''
'''
16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4
'''
'''
12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2
'''
