from collections import deque


def initialize():
    global bfs_queue
    bfs_queue = deque()

    for i in range(N):
        for j in range(N):
            visit[i][j] = False
            step[i][j] = -1


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def draw(new_r, new_c, island_num):
    bfs_queue.append((new_r, new_c))
    visit[new_r][new_c] = True
    island[new_r][new_c] = island_num


def draw_one_island(start_r, start_c, island_num):
    draw(start_r, start_c, island_num)

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()
        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c) and not visit[next_r][next_c] and grid[next_r][next_c] == 1:
                draw(next_r, next_c, island_num)


def draw_island():
    initialize()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and grid[i][j] == 1:
                cnt += 1
                draw_one_island(i, j, cnt)

    return cnt


def push(new_r, new_c, new_step):
    bfs_queue.append((new_r, new_c))
    visit[new_r][new_c] = True
    step[new_r][new_c] = new_step


def get_bridge(island_num):
    global answer

    for i in range(N):
        for j in range(N):
            if island[i][j] == island_num:
                push(i, j, 0)

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()
        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if not in_range(next_r, next_c):
                continue
            if visit[next_r][next_c]:
                continue
            if island[next_r][next_c] == island_num:
                continue

            if island[next_r][next_c] > 0:
                answer = min(answer, step[cur_r][cur_c])
                return
            if island[next_r][next_c] == 0:
                push(next_r, next_c, step[cur_r][cur_c] + 1)


def get_min_bridge(island_end_num):
    for island_num in range(1, island_end_num + 1):
        initialize()
        get_bridge(island_num)


def print_island():
    for i in range(N):
        for j in range(N):
            print(island[i][j], end=" ")
        print()
    print()


def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j], end=" ")
        print()
    print()


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
island = [[0] * N for _ in range(N)]

visit = [[False] * N for _ in range(N)]
step = [[-1] * N for _ in range(N)]
bfs_queue = ()

drs = [-1, 0, 1, 0]
dcs = [0, -1, 0, 1]

answer = N * N
island_cnt = draw_island()
# print_island()
get_min_bridge(island_cnt)
# print_step()
print(answer)


'''
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
'''
'''
5
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 1 0 0 1
'''
