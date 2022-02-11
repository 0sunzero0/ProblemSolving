from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [input().strip() for _ in range(N)]

visit = [[False] * N for _ in range(N)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(y, x):
    global group_cnt
    queue = deque()
    queue.append((y, x))
    group_cnt += 1
    visit[y][x] = True

    while queue:
        y, x = queue.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[ny][nx] == '1' and visit[ny][nx] == False:
                    queue.append((ny, nx))
                    group_cnt += 1
                    visit[ny][nx] = True

groups = []
group_cnt = 0
for y in range(N):
    for x in range(N):
        if graph[y][x] == '1' and visit[y][x] == False:
            group_cnt = 0
            bfs(y, x)
            groups.append(group_cnt)

groups.sort()
print(len(groups))
for group in groups:
    print(group)

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
