from collections import deque


def init():
    n, m = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    return n, m, grid


def get_virus_pos():
    result = list()
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                result.append((i, j))
    return result


def push(r, c, new_step):
    step[r][c] = new_step
    visit[r][c] = True
    bfs_queue.append((r, c))


def initialize(start_pos):
    for i in range(N):
        for j in range(N):
            step[i][j] = -1
            visit[i][j] = False

    for pos in start_pos:
        start_r, start_c = pos
        push(start_r, start_c, 0)


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def bfs():
    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]
    max_step = 0

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()
        if grid[cur_r][cur_c] == 0:
            max_step = max(step[cur_r][cur_c], max_step)

        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c) and not visit[next_r][next_c] and grid[next_r][next_c] != 1:
                push(next_r, next_c, step[cur_r][cur_c] + 1)

    return max_step


def is_all_virus():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0 and not visit[i][j]:
                return False
    return True


def get_min_time(idx, cnt):
    global answer, selected_pos

    if cnt == M:
        initialize(selected_pos)
        time = bfs()
        if is_all_virus():
            answer = min(time, answer)
        return

    if idx == len(virus_pos_list):
        return

    selected_pos.append(virus_pos_list[idx])
    get_min_time(idx + 1, cnt + 1)
    selected_pos.pop()
    get_min_time(idx + 1, cnt)


def print_answer():
    if answer == INT_MAX:
        print(-1)
    else:
        print(answer)


INT_MAX = 50 * 50 + 1
N, M, grid = init()

answer = INT_MAX
virus_pos_list = get_virus_pos()

bfs_queue = deque()
visit = [[False] * N for _ in range(N)]
step = [[-1] * N for _ in range(N)]

selected_pos = list()
get_min_time(0, 0)
print_answer()

'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''
'''
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
'''
'''
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
'''
