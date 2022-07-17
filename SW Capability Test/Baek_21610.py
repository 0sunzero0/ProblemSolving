N, M = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]
visit = [[False] * N for _ in range(N)]
cloud_pos = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]


def move_cloud():
    global cloud_pos
    dr = [0,  0,  -1, -1, -1, 0, 1, 1,  1]
    dc = [0, -1,  -1,  0,  1, 1, 1, 0, -1]

    new_cloud_pos = list()
    di, si = moves.pop(0)
    for r, c in cloud_pos:
        nr, nc = (r + dr[di] * si + N * si) % N, (c + dc[di] * si + N * si) % N
        new_cloud_pos.append((nr, nc))
        visit[nr][nc] = True
        grid[nr][nc] += 1

    return new_cloud_pos


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def magic():
    global cloud_pos
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    for r, c in cloud_pos:
        count = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if in_range(nr, nc) and grid[nr][nc] >= 1:
                count += 1
        grid[r][c] += count


def make_cloud():
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and grid[i][j] >= 2:
                grid[i][j] -= 2
                cloud_pos.append((i, j))


def simulate():
    global cloud_pos, visit
    visit = [[False] * N for _ in range(N)]
    cloud_pos = move_cloud()
    magic()
    cloud_pos = list()
    make_cloud()


def get_water_sum():
    result = 0
    for i in range(N):
        for j in range(N):
            result += grid[i][j]
    return result


for _ in range(M):
    simulate()
print(get_water_sum())

'''
5 4
0 0 1 0 2
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3
3 4
8 1
4 8
'''
'''
5 8
0 0 1 0 2
2 3 2 1 0
0 0 2 0 0
1 0 2 0 0
0 0 2 1 0
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
'''
'''
5 8
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
8 1
7 1
6 1
5 1
4 1
3 1
2 1
1 1
'''
