from collections import defaultdict, deque


def init():
    # N, M, K
    N, M, K = tuple(map(int, input().split()))
    # 활동할 영역의 지도
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 운전을 시작하는 칸의 행 번호와 열 번호
    taxi_r, taxi_c = tuple(map(int, input().split()))
    taxi_r -= 1
    taxi_c -= 1

    # 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호 M개
    passengers = [[0] * N for _ in range(N)]
    p_num2end = defaultdict(int)

    for p_num in range(1, M + 1):
        start_r, start_c, end_r, end_c = tuple(map(int, input().split()))
        start_r -= 1
        start_c -= 1
        end_r -= 1
        end_c -= 1

        passengers[start_r][start_c] = p_num
        p_num2end[p_num] = (end_r, end_c)

    return N, M, K, grid, taxi_r, taxi_c, passengers, p_num2end


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def choose():
    global taxi_fuel

    visit = [[False] * N for _ in range(N)]
    step = [[-1] * N for _ in range(N)]

    bfs_queue = deque([(taxi_r, taxi_c)])
    visit[taxi_r][taxi_c] = True
    step[taxi_r][taxi_c] = 0

    final_candidate = (N ** 2, N, N)

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()
        if passengers[cur_r][cur_c]:
            cur_candidate = (step[cur_r][cur_c], cur_r, cur_c)
            if cur_candidate < final_candidate:
                final_candidate = cur_candidate

        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c) and not visit[next_r][next_c] and grid[next_r][next_c] == 0:
                bfs_queue.append((next_r, next_c))
                visit[next_r][next_c] = True
                step[next_r][next_c] = step[cur_r][cur_c] + 1

    final_dist, final_r, final_c = final_candidate

    if final_candidate == (N ** 2, N, N):
        final_dist = -1

    return final_dist, final_r, final_c


def go_end(goal):
    global taxi_fuel

    visit = [[False] * N for _ in range(N)]
    step = [[-1] * N for _ in range(N)]

    bfs_queue = deque([(taxi_r, taxi_c)])
    visit[taxi_r][taxi_c] = True
    step[taxi_r][taxi_c] = 0

    while bfs_queue:
        cur_r, cur_c = bfs_queue.popleft()

        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c) and not visit[next_r][next_c] and grid[next_r][next_c] == 0:
                bfs_queue.append((next_r, next_c))
                visit[next_r][next_c] = True
                step[next_r][next_c] = step[cur_r][cur_c] + 1

    end_r, end_c = goal
    end_dist = step[end_r][end_c]

    return end_dist, end_r, end_c


def is_fuel(to_dist, to_r, to_c):
    global taxi_fuel, taxi_r, taxi_c
    if to_dist == -1 or taxi_fuel < to_dist:
        taxi_fuel = -1
        return False
    taxi_fuel, taxi_r, taxi_c = taxi_fuel - to_dist, to_r, to_c
    return True


def charge(dist):
    global taxi_fuel
    taxi_fuel += dist * 2


N, M, taxi_fuel, grid, taxi_r, taxi_c, passengers, p_num2end = init()
drs = [-1, 0, 1, 0]
dcs = [0, -1, 0, 1]

for _ in range(M):
    p_dist, p_r, p_c = choose()
    if not is_fuel(p_dist, p_r, p_c):
        break
    p_num = passengers[p_r][p_c]
    passengers[p_r][p_c] = 0
    end_dist, end_r, end_c = go_end(p_num2end[p_num])
    if not is_fuel(end_dist, end_r, end_c):
        break
    charge(end_dist)


print(taxi_fuel)

'''
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''
'''
6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''
'''
6 3 100
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''
