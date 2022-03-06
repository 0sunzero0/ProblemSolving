from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    is_united = False
    visited = [[False] * N for _ in range(N)]

    for i in range(0, N):
        for j in range(0, N):
            if visited[i][j] == False:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                united = deque()
                united.append((i, j))
                unit_population = graph[i][j]

                while queue:
                    y, x = queue.popleft()

                    for index in range(4):
                        ny, nx = y + dy[index], x + dx[index]
                        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == False:
                            if L <= abs(graph[y][x] - graph[ny][nx]) <= R:
                                queue.append((ny, nx))
                                visited[ny][nx] = True
                                united.append((ny, nx))
                                unit_population += graph[ny][nx]
                                is_united = True

                value = unit_population // len(united)
                while united:
                    y, x = united.popleft()
                    graph[y][x] = value

    return is_united

day = 0
while True:
    if bfs() == False:
        break
    day += 1

print(day)

'''
2 20 50
50 30
20 40
'''
