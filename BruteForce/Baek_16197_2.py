from collections import deque

N, M = tuple(map(int, input().split()))
grid = [ input().rstrip() for _ in range(N) ]
min_count = 11


def get_start_pos():
    coin_pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'o':
                coin_pos.append((i, j))

    return coin_pos


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x):
    if 0 <= y < N and 0 <= x < M:
        return not grid[y][x] == '#'
    return True


def bfs():
    global min_count

    bfs_queue = deque()
    y1, x1 = coin1_start_pos
    y2, x2 = coin2_start_pos
    bfs_queue.append((y1, x1, y2, x2, 0))

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    while bfs_queue:
        y1, x1, y2, x2, count = bfs_queue.popleft()

        if count > 10:
            continue

        if not in_range(y1, x1) and not in_range(y2, x2):
            continue

        elif not in_range(y1, x1) or not in_range(y2, x2):
            min_count = min(min_count, count)
            continue

        for dy, dx in zip(dys, dxs):
            ny1, nx1 = y1 + dy, x1 + dx
            ny2, nx2 = y2 + dy, x2 + dx
            if can_go(ny1, nx1) and can_go(ny2, nx2):
                bfs_queue.append((ny1, nx1, ny2, nx2, count + 1))
            elif can_go(ny1, nx1):
                bfs_queue.append((ny1, nx1, y2, x2, count + 1))
            elif can_go(ny2, nx2):
                bfs_queue.append((y1, x1, ny2, nx2, count + 1))


coin1_start_pos, coin2_start_pos = get_start_pos()
bfs()

if min_count == 11:
    print(-1)
else:
    print(min_count)

'''
1 2
oo
'''
'''
6 2
..
..
..
o#
o#
##
'''
