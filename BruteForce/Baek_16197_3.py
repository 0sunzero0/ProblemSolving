from collections import deque

N, M = tuple(map(int, input().split()))
grid = [ input().rstrip() for _ in range(N) ]


def get_start_pos():
    coin_pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'o':
                coin_pos.append((i, j))

    return coin_pos


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def is_wall(y, x):
    return grid[y][x] == '#'


def bfs():
    bfs_queue = deque()
    y1, x1 = coin1_start_pos
    y2, x2 = coin2_start_pos
    bfs_queue.append((y1, x1, y2, x2, 0))

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    while bfs_queue:
        y1, x1, y2, x2, count = bfs_queue.popleft()
        if count > 10:
            return -1

        for dy, dx in zip(dys, dxs):
            ny1, nx1 = y1 + dy, x1 + dx
            ny2, nx2 = y2 + dy, x2 + dx

            if in_range(ny1, nx1) and in_range(ny2, nx2):
                if is_wall(ny1, nx1):
                    ny1, nx1 = y1, x1
                if is_wall(ny2, nx2):
                    ny2, nx2 = y2, x2
                bfs_queue.append((ny1, nx1, ny2, nx2, count + 1))
            elif in_range(ny1, nx1):
                return count + 1
            elif in_range(ny2, nx2):
                return count + 1


coin1_start_pos, coin2_start_pos = get_start_pos()
print(bfs())

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
