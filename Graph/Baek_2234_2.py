from collections import deque

C, R = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]


def in_range(y, x):
    return 0 <= y < R and 0 <= x < C


def can_go(ni, nj, i, j, k):
    return in_range(ni, nj) and visited[ni][nj] == 0 and grid[i][j] & (1 << k) == 0


def bfs(sy, sx, num):
    dys, dxs = [0, -1, 0, 1], [-1, 0, 1, 0]
    bfs_queue = deque()

    visited[sy][sx] = num
    bfs_queue.append((sy, sx))

    while bfs_queue:
        y, x = bfs_queue.popleft()
        for di in range(4):
            ny, nx = dys[di] + y, dxs[di] + x
            if can_go(ny, nx, y, x, di):
                visited[ny][nx] = num
                bfs_queue.append((ny, nx))


def get_room_num():
    count = 0
    for i in range(R):
        for j in range(C):
            if visited[i][j] == 0:
                count += 1
                bfs(i, j, count)
    return count


def get_room_areas(room_num):
    count = [0] * (room_num + 1)
    for i in range(R):
        for j in range(C):
            count[visited[i][j]] += 1
    return count


def get_max_removed_room_area(room_areas):
    dys, dxs = [0, -1, 0, 1], [-1, 0, 1, 0]
    result = 0

    for i in range(R):
        for j in range(C):
            y, x = i, j
            for di in range(4):
                ny, nx = y + dys[di], x + dxs[di]
                if not in_range(ny, nx):
                    continue
                if visited[ny][nx] == visited[y][x]:
                    continue
                if (grid[y][x] & (1 << di)) > 0:
                    if result < room_areas[visited[y][x]] + room_areas[visited[ny][nx]]:
                        result = room_areas[visited[y][x]] + room_areas[visited[ny][nx]]
    return result


def get_answer():
    room_num = get_room_num()
    print(room_num)
    room_areas = get_room_areas(room_num)
    print(max(room_areas))
    print(get_max_removed_room_area(room_areas))


get_answer()

'''
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
'''
