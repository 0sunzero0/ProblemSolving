from collections import deque

MAX_INT = 1000 * 1000 + 1
N, M = tuple(map(int, input().split()))
grid = [list(map(int, list(input()))) for _ in range(N)]
dist = [[[-1] * 2 for _ in range(M)] for _ in range(N)]


def in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def can_go_wall(r, c, count):
    return in_range(r, c) and count == 0 and grid[r][c] == 1 and dist[r][c][count + 1] == -1


def can_go_blank(r, c, count):
    return in_range(r, c) and grid[r][c] == 0 and dist[r][c][count] == -1


def bfs(sy, sx):
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append((sy, sx, 0))
    dist[sy][sx][0] = 1

    while queue:
        y, x, count = queue.popleft()
        for i in range(4):
            ny, nx = y + dys[i], x + dxs[i]
            # 벽이 없다면
            if can_go_blank(ny, nx, count):
                dist[ny][nx][count] = dist[y][x][count] + 1
                queue.append((ny, nx, count))
            # 벽이 있다면
            if can_go_wall(ny, nx, count):
                dist[ny][nx][count + 1] = dist[y][x][count] + 1
                queue.append((ny, nx, count + 1))


bfs(0, 0)

if dist[N - 1][M - 1][0] == -1:
    dist[N - 1][M - 1][0] = MAX_INT
if dist[N - 1][M - 1][1] == -1:
    dist[N - 1][M - 1][1] = MAX_INT
answer = min(dist[N - 1][M - 1])

if answer == MAX_INT:
    print(-1)
else:
    print(answer)

'''
6 4
0100
1110
1000
0000
0111
0000
'''
