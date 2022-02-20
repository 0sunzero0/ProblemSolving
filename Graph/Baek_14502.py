from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_safe_area = 0
virus_queue = deque()

def get_safe_area():
    visited = [[0] * M for _ in range(N)] # virus가 갈 수 있으면, 방문

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                visited[i][j] = 1
                virus_queue.append((i, j))

    while virus_queue:
        y, x = virus_queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] == 0:
                visited[ny][nx] = 1
                virus_queue.append((ny, nx))

    zero_count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and visited[i][j] == 0:
                zero_count += 1
    return zero_count

def simulate(wall_count):
    global max_safe_area

    if wall_count == 3:
        safe_area = get_safe_area()
        max_safe_area = max(max_safe_area, safe_area)
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                simulate(wall_count + 1)
                graph[i][j] = 0

simulate(0)
print(max_safe_area)
