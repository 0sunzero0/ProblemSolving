from collections import deque

N, M = tuple(map(int, input().split()))
grid = [list(input().strip()) for _ in range(N)]


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(start_r, start_c):
    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]

    visit = [[0] * M for _ in range(N)]
    bfs_deque = deque()

    visit[start_r][start_c] = 1
    bfs_deque.append((start_r, start_c))

    cnt = 0
    while bfs_deque:
        cur_r, cur_c = bfs_deque.popleft()
        for dr, dc in zip(drs, dcs):
            next_r, next_c = cur_r + dr, cur_c + dc
            if in_range(next_r, next_c):
                if grid[next_r][next_c] == 'L' and not visit[next_r][next_c]:
                    visit[next_r][next_c] = visit[cur_r][cur_c] + 1
                    bfs_deque.append((next_r, next_c))
                    cnt = max(cnt, visit[next_r][next_c])
    return cnt - 1


answer = 0
for r in range(N):
    for c in range(M):
        if grid[r][c] == 'L':
            answer = max(answer, bfs(r, c))

print(answer)

'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
'''
