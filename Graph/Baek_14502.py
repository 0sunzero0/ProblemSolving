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


for y1 in range(N):
    for x1 in range(M):
        if graph[y1][x1] != 0:
            continue
        for y2 in range(N):
            for x2 in range(M):
                if graph[y2][x2] != 0:
                    continue
                for y3 in range(N):
                    for x3 in range(M):
                        if graph[y3][x3] != 0:
                            continue

                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue

                        graph[y1][x1] = 1
                        graph[y2][x2] = 1
                        graph[y3][x3] = 1

                        safe_area = get_safe_area()
                        max_safe_area = max(safe_area, max_safe_area)

                        graph[y1][x1] = 0
                        graph[y2][x2] = 0
                        graph[y3][x3] = 0

print(max_safe_area)
