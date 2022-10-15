from collections import deque

RAINBOW = 0
BLACK = -1
EMPTY = -2
EMPTY_GROUP = (-1, -1, -1, -1)


def init():
    n, m = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid


def initialize_visit():
    for i in range(N):
        for j in range(N):
            visit[i][j] = False


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def can_go(r, c, target_num):
    return in_range(r, c) and not visit[r][c] and (grid[r][c] == RAINBOW or grid[r][c] == target_num)


def bfs(start_r, start_c, target_num):
    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]

    initialize_visit()
    visit[start_r][start_c] = True
    bfs_q.append((start_r, start_c))

    while bfs_q:
        cur_r, cur_c = bfs_q.popleft()

        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc

            if can_go(next_r, next_c, target_num):
                bfs_q.append((next_r, next_c))
                visit[next_r][next_c] = True


def get_block_group(r, c):
    bfs(r, c, grid[r][c])

    block_cnt, rainbow_cnt = 0, 0
    standard = (N, N)

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                continue
            block_cnt += 1

            if grid[i][j] == RAINBOW:
                rainbow_cnt += 1
            elif (i, j) < standard:
                standard = (i, j)

    std_r, std_c = standard

    return (block_cnt, rainbow_cnt, std_r, std_c)


def find_best_block_group():
    max_block_group = EMPTY_GROUP

    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 1:
                cur_block_group = get_block_group(i, j)
                if cur_block_group > max_block_group:
                    max_block_group = cur_block_group

    return max_block_group


def clear(r, c):
    bfs(r, c, grid[r][c])

    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                grid[i][j] = EMPTY


def gravity():
    next_grid = [[EMPTY] * N for _ in range(N)]

    for j in range(N):
        last_idx = N - 1
        for i in range(N - 1, -1, -1):
            if grid[i][j] == EMPTY:
                continue
            if grid[i][j] == BLACK:
                last_idx = i
            next_grid[last_idx][j] = grid[i][j]
            last_idx -= 1

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]


def rotate_by_90_degree():
    next_grid = [[EMPTY] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            next_grid[N - 1 - j][i] = grid[i][j]

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]


N, M, grid = init()
score = 0
visit = [[False] * N for _ in range(N)]
bfs_q = deque()

while True:
    best_block_group = find_best_block_group()
    block_cnt, _, standard_r, standard_c = best_block_group

    if best_block_group == EMPTY_GROUP or block_cnt <= 1:
        break

    clear(standard_r, standard_c)
    score += block_cnt * block_cnt

    gravity()
    rotate_by_90_degree()
    gravity()

print(score)

'''
5 3
2 2 -1 3 1
3 3 2 0 -1
0 0 0 1 2
-1 3 1 3 2
0 3 2 2 1
'''
'''
6 4
2 3 1 0 -1 2
2 -1 4 1 3 3
3 0 4 2 2 1
-1 4 -1 2 3 4
3 -1 4 2 0 3
1 2 2 2 2 1
'''
