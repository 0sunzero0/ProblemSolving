from collections import deque

N, M = map(int, input().split())
graph = [input().strip() for _ in range(N)]
distance = [[0] * M for _ in range(N)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs():
    queue = deque()
    queue.append((0, 0))
    distance[0][0] = 1

    while queue:
        y, x = queue.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == '1' and distance[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x] + 1
                    queue.append((ny, nx))


bfs()
print(distance[N-1][M-1])
'''
4 6
101111
101010
101011
111011
'''
