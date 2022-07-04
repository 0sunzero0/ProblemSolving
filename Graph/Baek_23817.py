from collections import deque
import sys
input = sys.stdin.readline


def get_start_pos():
    result = []
    count = 1

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'K':
                result.append((i, j))
                grid[i][j] = count
                count += 1
            elif grid[i][j] == 'S':
                grid[i][j] = 0

    return result, count


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x, dist):
    return in_range(y, x) and dist[y][x] == -1 and grid[y][x] != 'X'


def bfs(sy, sx, idx):
    global graph

    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    dist = [[-1] * M for _ in range(N)]

    dist[sy][sx] = 0
    queue = deque([(sy, sx)])

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dys[i], x + dxs[i]

            if can_go(ny, nx, dist):
                dist[ny][nx] = dist[y][x] + 1

                if type(grid[ny][nx]) == int:
                    graph[idx].add((grid[ny][nx], dist[ny][nx]))
                    graph[grid[ny][nx]].add((idx, dist[ny][nx]))

                queue.append((ny, nx))


def make_graph():
    for idx, pos in enumerate(start_pos):
        y, x = pos
        bfs(y, x, idx + 1)


def go(current_vertex, count, time):
    global answer
    if answer <= time:
        return

    if count == 5:
        answer = min(time, answer)
        return

    visited[current_vertex] = True
    for next_vertex, cost in graph[current_vertex]:
        if not visited[next_vertex]:
            go(next_vertex, count + 1, time + cost)
    visited[current_vertex] = False


N, M = tuple(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(N)]

start_pos, count = get_start_pos()
graph = [set() for _ in range(count)]
make_graph()

if len(graph[0]) < 5:
    print(-1)
    exit()

visited = [0] * count
answer = float("inf")
go(0, 0, 0)
print(answer)

'''
4 4
SKKK
X..X
X..X
K..K
'''
'''
4 4
SKKK
XXXX
KKKK
KKKK
'''
