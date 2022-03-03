import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = [[input().split() for _ in range(N)] for _ in range(H)]
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
dx = [-1,  1,  0,  0,  0,  0]
dy = [ 0,  0, -1,  1,  0,  0]
dz = [ 0,  0,  0,  0, -1,  1]
queue = deque()
date = 0

def set_start_point():
    for z in range(0, H):
        for y in range(0, N):
            for x in range(0, M):
                if graph[z][y][x] == '1':
                    queue.append((z, y, x))
                    visited[z][y][x] += 1

def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if graph[nz][ny][nx] == '0' and visited[nz][ny][nx] == -1:
                    graph[nz][ny][nx] = '1'
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    queue.append((nz, ny, nx))

def is_all_ripen():
    global date
    for z in range(0, H):
        for y in range(0, N):
            for x in range(0, M):
                if graph[z][y][x] == '0':
                    return False
                date = max(int(visited[z][y][x]), date)
    return True

set_start_point()
bfs()
if is_all_ripen():
    print(date)
else:
    print(-1)
