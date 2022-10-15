from collections import deque

N = int(input())
grid = [ list(map(int, input().split())) for _ in range(N) ]

time = 0
shark_size = 2
ate = 0
shark_y, shark_x = 0, 0

visited = [ [-1] * N for _ in range(N) ]


def get_start_pos():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                return i, j


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def can_go(y, x):
    return in_range(y, x) and visited[y][x] == -1 and 0 <= grid[y][x] <= shark_size


def can_eat(y, x):
    return 1 <= grid[y][x] < shark_size


def move_shark():
    global visited, shark_y, shark_x, ate, time

    visited = [ [-1] * N for _ in range(N) ]
    queue = deque()
    queue.append((shark_y, shark_x))
    visited[shark_y][shark_x] = 0

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = dy + y, dx + x
            if can_go(ny, nx):
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    can_shark_eat = False
    min_dist = 20 * 20

    for i in range(N):
        for j in range(N):
            if 1 <= visited[i][j] < min_dist and can_eat(i, j):
                can_shark_eat = True
                shark_y, shark_x = i, j
                min_dist = visited[i][j]

    if can_shark_eat:
        ate += 1
        grid[shark_y][shark_x] = 0
        time += min_dist

    return can_shark_eat


def simulate():
    global shark_size, ate
    can_shark_eat = move_shark()
    if shark_size == ate:
        shark_size += 1
        ate = 0

    return can_shark_eat


shark_y, shark_x = get_start_pos()
grid[shark_y][shark_x] = 0

while True:
    if not simulate():
        break

print(time)

'''
3
0 0 1
0 0 0
0 9 0
'''
