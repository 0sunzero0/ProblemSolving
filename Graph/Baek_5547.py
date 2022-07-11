from collections import deque

W, H = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(H)]


def move(y, x, dir):
    if dir == 0:
        if y % 2 == 1: return (y - 1, x - 1)
        return (y - 1, x)
    if dir == 1:
        if y % 2 == 1: return (y - 1, x)
        return (y - 1, x + 1)
    if dir == 2:
        return (y, x + 1)
    if dir == 3:
        if y % 2 == 1: return (y + 1, x)
        return (y + 1, x + 1)
    if dir == 4:
        if y % 2 == 1: return (y + 1, x - 1)
        return (y + 1, x)
    if dir == 5:
        return (y, x - 1)


def in_range(i, j):
    return 0 <= i < H and 0 <= j < W


def bfs_outside(sy, sx):
    bfs_queue = deque()
    bfs_queue.append((sy, sx))
    grid[sy][sx] = 2
    visit[sy][sx] = True

    while bfs_queue:
        y, x = bfs_queue.popleft()
        grid[y][x] = 2
        for dir in range(6):
            ny, nx = move(y, x, dir)
            if in_range(ny, nx):
                if not visit[ny][nx] and grid[ny][nx] != 1:
                    bfs_queue.append((ny, nx))
                    visit[ny][nx] = True


def make_outside():
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1:
                continue
            if i == 0 or j == 0 or i == H - 1 or j == W - 1:
                if not visit[i][j]:
                    bfs_outside(i, j)


def bfs_building(sy, sx):
    global count
    bfs_queue = deque()
    bfs_queue.append((sy, sx))
    visit[sy][sx] = True

    while bfs_queue:
        y, x = bfs_queue.popleft()

        for dir in range(6):
            ny, nx = move(y, x, dir)
            if in_range(ny, nx):
                if not visit[ny][nx] and grid[ny][nx] == 1:
                    bfs_queue.append((ny, nx))
                    visit[ny][nx] = True
            if not in_range(ny, nx) or grid[ny][nx] == 2:
                count += 1

    return count


def count_wall_boarder():
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1:
                if not visit[i][j]:
                    bfs_building(i, j)


visit = [[False] * W for _ in range(H)]
make_outside()
visit = [[False] * W for _ in range(H)]
count = 0
count_wall_boarder()
print(count)

'''
8 4
0 1 0 1 0 1 1 1
0 1 1 0 0 1 0 0
1 0 1 0 1 1 1 1
0 1 1 0 1 0 1 0
'''
'''
8 5
0 1 1 1 0 1 1 1
0 1 0 0 1 1 0 0
1 0 0 1 1 1 1 1
0 1 0 1 1 0 1 0
0 1 1 0 1 1 0 0
'''
