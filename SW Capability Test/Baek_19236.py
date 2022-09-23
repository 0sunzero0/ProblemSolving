def init():
    grid = [[(0, 0) for _ in range(N)] for _ in range(N)]

    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            grid[r][c] = (row[2 * c], row[2 * c + 1] - 1)

    return grid


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def fish_can_go(r, c):
    return in_range(r, c) and grid[r][c] != SHARK


def get_next(cur_r, cur_c, cur_dir):
    for di in range(DIR_NUM):
        next_dir = (cur_dir + di) % DIR_NUM
        next_r, next_c = cur_r + drs[next_dir], cur_c + dcs[next_dir]
        if fish_can_go(next_r, next_c):
            return next_r, next_c, next_dir
    return cur_r, cur_c, cur_dir


def swap(cur_r, cur_c, next_r, next_c):
    grid[cur_r][cur_c], grid[next_r][next_c] = grid[next_r][next_c], grid[cur_r][cur_c]


def move_fish(target_num):
    for fish_r in range(N):
        for fish_c in range(N):
            fish_num, fish_dir = grid[fish_r][fish_c]
            if fish_num == target_num:
                next_r, next_c, next_dir = get_next(fish_r, fish_c, fish_dir)
                grid[fish_r][fish_c] = (fish_num, next_dir)
                swap(fish_r, fish_c, next_r, next_c)
                return


def move_all_fish():
    for fish_num in range(1, N * N + 1):
        move_fish(fish_num)


def shark_can_go(r, c):
    return in_range(r, c) and grid[r][c] != BLANK


def is_complete(cur_r, cur_c, cur_dir):
    for step in range(1, N):
        next_r, next_c = cur_r + drs[cur_dir] * step, cur_c + dcs[cur_dir] * step
        if shark_can_go(next_r, next_c):
            return False
    return True


def get_max_fish_sum(cur_r, cur_c, cur_dir, cur_fish_sum):
    global answer
    answer = max(answer, cur_fish_sum)

    temp_grid = [
                    [grid[r][c] for c in range(N)]
                    for r in range(N)
                ]

    for step in range(1, N):
        next_r, next_c = cur_r + drs[cur_dir] * step, cur_c + dcs[cur_dir] * step

        if shark_can_go(next_r, next_c):

            extra_fish_sum, next_dir = grid[next_r][next_c]
            grid[cur_r][cur_c], grid[next_r][next_c] = BLANK, SHARK

            move_all_fish()
            get_max_fish_sum(next_r, next_c, next_dir, cur_fish_sum + extra_fish_sum)

            for r in range(N):
                for c in range(N):
                    grid[r][c] = temp_grid[r][c]


answer = 0

N = 4
DIR_NUM = 8

drs = [-1, -1, 0, 1, 1, 1, 0, -1]
dcs = [0, -1, -1, -1, 0, 1, 1, 1]

BLANK = (0, 0)
SHARK = (-1, -1)
grid = init()

init_fish_sum, init_dir = grid[0][0]
grid[0][0] = SHARK

move_all_fish()

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
