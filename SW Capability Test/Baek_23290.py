def init():
    m, s = tuple(map(int, input().split()))
    input_grid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for _ in range(m):
        fish_r, fish_c, fish_dir = tuple(map(int, input().split()))
        fish_r, fish_c, fish_dir = fish_r - 1, fish_c - 1, fish_dir - 1
        input_grid[fish_r][fish_c].append(fish_dir)

    sr, sc = tuple(map(int, input().split()))
    sr, sc = sr - 1, sc - 1

    return m, s, input_grid, sr, sc


def magic_copy():
    copy_fish = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            for element in grid[i][j]:
                copy_fish[i][j].append(element)

    return copy_fish


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def get_next(cur_r, cur_c, cur_dir):
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    drs = [0,  -1, -1, -1, 0, 1, 1,  1]
    dcs = [-1, -1,  0,  1, 1, 1, 0, -1]

    for delta in range(FISH_DIR_NUM):
        next_dir = (cur_dir - delta) % FISH_DIR_NUM
        next_r, next_c = cur_r + drs[next_dir], cur_c + dcs[next_dir]
        if in_range(next_r, next_c):
            if (next_r, next_c) != (shark_r, shark_c) and smell[next_r][next_c] == 0:
                return next_r, next_c, next_dir
    return cur_r, cur_c, cur_dir


def move_fish():
    next_grid = [
        [[] for _ in range(N)]
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            for element in grid[i][j]:
                next_i, next_j, next_dir = get_next(i, j, element)
                next_grid[next_i][next_j].append(next_dir)

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]


def get_fish_num(dir1, dir2, dir3):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    r, c = shark_r, shark_c
    predicted_fish_num = 0

    # 방문한 적이 있는지를 기록
    visited_position = set()

    for move_dir in [dir1, dir2, dir3]:
        next_r, next_c = r + dr[move_dir], c + dc[move_dir]

        # 움직이는 도중에 격자를 벗어나면 선택되면 안된다.
        if not in_range(next_r, next_c):
            return -1

        # 이미 계산한 곳에 대해서는 중복 계산하지 않는다.
        if (next_r, next_c) not in visited_position:
            predicted_fish_num += len(grid[next_r][next_c])
            visited_position.add((next_r, next_c))

        r, c = next_r, next_c

    return predicted_fish_num


def move_shark():
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    max_count = -1
    best_route = (-1, -1, -1)

    for i in range(SHARK_DIR_NUM):
        for j in range(SHARK_DIR_NUM):
            for k in range(SHARK_DIR_NUM):
                current_count = get_fish_num(i, j, k)
                if current_count > max_count:
                    max_count = current_count
                    best_route = (i, j, k)

    global shark_r, shark_c
    dir1, dir2, dir3 = best_route
    for move_dir in [dir1, dir2, dir3]:
        next_r, next_c = shark_r + dr[move_dir], shark_c + dc[move_dir]
        # 물고기가 존재하면, 물고기를 격자에서 제외하고 냄새를 남긴다.
        if len(grid[next_r][next_c]) > 0:
            smell[next_r][next_c] = 3
            grid[next_r][next_c] = list()
        shark_r, shark_c = next_r, next_c


def disappear_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j] > 0:
                smell[i][j] -= 1


def complete_copy(copy_fish):
    for i in range(N):
        for j in range(N):
            for element in copy_fish[i][j]:
                grid[i][j].append(element)


def simulate():
    copy_fish = magic_copy()
    # print("step1")
    # print_grid()
    # print(shark_r, shark_c)
    move_fish()
    # print("step2")
    # print_grid()
    # print(shark_r, shark_c)
    move_shark()
    # print("step3")
    # print_grid()
    # print(shark_r, shark_c)
    disappear_smell()
    # print("step4")
    # print_smell()
    # print(shark_r, shark_c)
    complete_copy(copy_fish)
    # print("step5")
    # print_grid()
    # print(shark_r, shark_c)


def pro():
    for _ in range(S):
        simulate()


def print_answer():
    count = 0
    for i in range(N):
        for j in range(N):
            for _ in grid[i][j]:
                count += 1
    print(count)


def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()


def print_smell():
    for i in range(N):
        for j in range(N):
            print(smell[i][j], end=" ")
        print()


N = 4
FISH_DIR_NUM = 8
SHARK_DIR_NUM = 4

smell = [[0] * N for _ in range(N)]
M, S, grid, shark_r, shark_c = init()
pro()
print_answer()

'''
5 1
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
'''
'''
5 2
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
'''
'''
5 3
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
'''
