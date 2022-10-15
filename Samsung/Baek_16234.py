from collections import deque

N, L, R = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]


def in_range(y, x):
   return 0 <= y < N and 0 <= x < N


def can_go(ny, nx, y, x):
    return L <= abs(grid[ny][nx] - grid[y][x]) <= R and not visit[ny][nx]


def bfs_unit(sy, sx):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    bfs_queue = deque()
    visit[sy][sx] = True
    bfs_queue.append((sy, sx))

    count = 1
    populations = grid[sy][sx]
    pos = [(sy, sx)]

    while bfs_queue:
        y, x = bfs_queue.popleft()
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if in_range(ny, nx) and can_go(ny, nx, y, x):
                count += 1
                populations += grid[ny][nx]
                pos.append((ny, nx))

                visit[ny][nx] = True
                bfs_queue.append((ny, nx))

    return count, populations, pos


def simulate():
    global unit_count

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                count, populations, pos = bfs_unit(i, j)
            for y, x in pos:
                grid[y][x] = populations // count
            if count >= 2:
                unit_count += 1


time = 0

while True:
    visit = [[False] * N for _ in range(N)]
    unit_count = 0
    simulate()
    if unit_count == 0:
        break
    time += 1

print(time)

'''
2 20 50
50 30
20 40
'''
