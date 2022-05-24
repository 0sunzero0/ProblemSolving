from collections import deque

N, M = tuple(map(int, input().split()))
grid = [ list(map(int, input().split())) for _ in range(N) ]

max_safe_area = 0
# 빈칸 위치
blank_pos = []
# 바이러스 위치
virus_pos = []

temp = []
visited = [ [False] * M for _ in range(N) ]

for i in range(N):
    for j in range(M):
        # 빈칸
        if grid[i][j] == 0:
            blank_pos.append((i, j))
        # 바이러스
        elif grid[i][j] == 2:
            virus_pos.append((i, j))


def get_safe_area():
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                count += 1
    return count


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x):
    return in_range(y, x) and temp[y][x] == 0 and not visited[y][x]


def bfs(start_y, start_x):
    global visited
    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True

    while queue:
        y, x = queue.popleft()
        for dy, dx in zip(dys, dxs):
            ny, nx = dy + y, x + dx
            if can_go(ny, nx):
                queue.append((ny, nx))
                visited[ny][nx] = True
                temp[ny][nx] = 2


def spread():
    global temp, visited

    temp = [
        [grid[i][j] for j in range(M)]
        for i in range(N)
    ]

    visited = [
        [False] * M
        for _ in range(N)
    ]

    for y, x in virus_pos:
        if not visited[y][x]:
            bfs(y, x)


def make_wall():
    global max_safe_area

    for i in range(0, len(blank_pos)):
        for j in range(i + 1, len(blank_pos)):
            for k in range(j + 1, len(blank_pos)):
                selected_pos = [ blank_pos[i], blank_pos[j], blank_pos[k] ]

                for y, x in selected_pos:
                    grid[y][x] = 1

                spread()
                max_safe_area= max(max_safe_area, get_safe_area())

                for y, x in selected_pos:
                    grid[y][x] = 0


make_wall()
print(max_safe_area)

'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
'''
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
'''
'''
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''
