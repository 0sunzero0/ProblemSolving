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


def get_max_room_area(room_num):
    count = [0] * (room_num + 1)
    for i in range(R):
        for j in range(C):
            count[visited[i][j]] += 1
    return max(count)


def get_max_removed_room_area():
    global visited
    result = 0

    for i in range(R):
        for j in range(C):
            for k in (1 << 0, 1 << 1, 1 << 2, 1 << 3):
                if grid[i][j] & k:
                    grid[i][j] -= k

                    visited = [[0] * C for _ in range(R)]
                    removed_room_num = get_room_num()
                    result = max(result, get_max_room_area(removed_room_num))

                    grid[i][j] += k
    return result


def get_answer():
    room_num = get_room_num()
    print(room_num)
    print(get_max_room_area(room_num))
    print(get_max_removed_room_area())


get_answer()

'''
7 4
11 6 11 6 3 10 6
7 9 6 13 5 15 5
1 10 12 7 13 7 5
13 11 10 8 10 12 13
'''
