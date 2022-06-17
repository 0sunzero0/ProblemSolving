N, M = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]

MAX_INT = N * M
answer = MAX_INT

cctv_pos = [
    (i, j)
    for i in range(N)
    for j in range(M)
    if grid[i][j] != 0 and grid[i][j] != 6
]
cctv_num = len(cctv_pos)
selected_cctv_dir = []
can_move = [
    [],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
visited = [[False] * M for _ in range(N)]


def rotate(idx, current_dir):
    return (idx + current_dir) % 4


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x):
    return in_range(y, x) and grid[y][x] != 6


def fill(start_y, start_x, idx):
    cctv_type = grid[start_y][start_x]
    cctv_dir = selected_cctv_dir[idx]

    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]

    for i in range(4):
        if not can_move[cctv_type][i]:
            continue

        y, x = start_y, start_x
        move_dir = rotate(i, cctv_dir)

        while True:
            visited[y][x] = True
            ny, nx = y + dys[move_dir], x + dxs[move_dir]
            if can_go(ny, nx):
                y, x = ny, nx
            else:
                break


def fill_cctv_area():
    for idx, pos in enumerate(cctv_pos):
        y, x = pos
        fill(y, x, idx)


def get_blind_area():
    global visited
    visited = [[False] * M for _ in range(N)]
    fill_cctv_area()

    area = sum([
        1
        for i in range(N)
        for j in range(M)
        if not visited[i][j] and grid[i][j] != 6
    ])
    return area


def combination(current_idx):
    global selected_cctv_dir, answer

    if current_idx == cctv_num:
        answer = min(answer, get_blind_area())
        return

    for direction in range(0, 4):
        selected_cctv_dir.append(direction)
        combination(current_idx + 1)
        selected_cctv_dir.pop()


combination(0)
print(answer)

'''
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
'''
'''
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
'''
'''
1 7
0 1 2 3 4 5 6
'''
