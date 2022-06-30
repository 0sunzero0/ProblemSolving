from collections import deque

R, C = tuple(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(R)]
dist = [[-1] * C for _ in range(R)]
water_time = [[50 * 50] * C for _ in range(R)]


def get_pos():
    water_pos = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'D':
                final_pos = (i, j)
            elif grid[i][j] == '*':
                water_pos.append((i, j))

    return start_pos, final_pos, water_pos


start_pos, final_pos, water_pos = get_pos()


def in_range(y, x):
    return 0 <= y < R and 0 <= x < C


def water_can_go(y, x):
    return in_range(y, x) and water_time[y][x] == 50 * 50 and grid[y][x] != 'D' and grid[y][x] != 'X'


def go_water():
    # water
    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]
    water_queue = deque()

    for one_water_pos in water_pos:
        y, x = one_water_pos
        water_time[y][x] = 0
        water_queue.append((y, x))

    while water_queue:
        y, x = water_queue.popleft()
        for i in range(4):
            ny, nx = y + dys[i], x + dxs[i]
            if water_can_go(ny, nx):
                water_time[ny][nx] = water_time[y][x] + 1
                water_queue.append((ny, nx))


def animal_can_go(ni, nj, i, j):
    return in_range(ni, nj) and dist[ni][nj] == -1 and water_time[ni][nj] > dist[i][j] + 1 and grid[ni][nj] != '*' and grid[ni][nj] != 'X'


def go_animal():
    # animal
    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]
    animal_queue = deque()

    sy, sx = start_pos
    dist[sy][sx] = 0
    animal_queue.append((sy, sx))

    while animal_queue:
        y, x = animal_queue.popleft()
        for i in range(4):
            ny, nx = y + dys[i], x + dxs[i]
            if animal_can_go(ny, nx, y, x):
                dist[ny][nx] = dist[y][x] + 1
                animal_queue.append((ny, nx))


def go():
    go_water()
    go_animal()


go()
if dist[final_pos[0]][final_pos[1]] == -1:
    print("KAKTUS")
else:
    print(dist[final_pos[0]][final_pos[1]])

'''
3 3
D.*
...
.S.
'''
