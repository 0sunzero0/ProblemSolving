from collections import deque

N = int(input())
graph = [input().strip() for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    count = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == '1' and visited[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = 1
                count += 1

    apart_nums.append(count)

group_count = 0
apart_nums = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == '1' and visited[y][x] == 0:
            bfs(y, x)
            group_count += 1

apart_nums.sort()
print(group_count)
for apart_num in apart_nums:
    print(apart_num)

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
