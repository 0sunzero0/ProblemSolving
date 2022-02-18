from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
hour = 0
cheese_queue = deque()

def init():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == -1:
                graph[i][j] = 0
            if visited[i][j] == 1:
                visited[i][j] = 0

def melt_cheese():
    while cheese_queue:
        y, x = cheese_queue.popleft()

        contacted_grid_count = 0
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == -1:
                    contacted_grid_count += 1
        if contacted_grid_count >= 2:
            graph[y][x] = 0

def make_outair():
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1:
                    cheese_queue.append((ny, nx))
                    visited[ny][nx] = 1
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    queue.append((ny, nx))
                    graph[ny][nx] = -1
                    visited[ny][nx] = 1

def get_meltpos():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return i, j
    else:
        return None

while True:
    pos = get_meltpos()
    if pos == None:
        print(hour)
        break

    make_outair()
    melt_cheese()
    hour += 1
    init()

'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''
