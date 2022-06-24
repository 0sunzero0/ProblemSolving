import sys

DIR_NUM = 4
N, K = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
horses_info = [list(map(int, input().split())) for _ in range(K)]
horses_grid = [[[] for _ in range(N)] for _ in range(N)]


for idx, horse_info in enumerate(horses_info):
    a, b, c = horse_info
    horses_grid[a - 1][b - 1] = [idx]
    horses_info[idx] = [a - 1, b - 1, c - 1]


def is_more_four(i, j):
    return len(horses_grid[i][j]) >= 4


def reverse_order(arr):
    return arr[::-1]


def change_dir(current_dir):
    if 0 <= current_dir <= 1:
        return (current_dir + 1) % 2
    else:
        return (current_dir + 1) % 2 + 2


def push(ni, nj, i, j):
    horse_nums = horses_grid[i][j]
    for num in horse_nums:
        horses_grid[ni][nj].append(num)
        horses_info[num][:2] = [ni, nj]
    horses_grid[i][j] = []


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


def move(num):
    # →, ←, ↑, ↓
    dys = [0, 0, -1, 1]
    dxs = [1, -1, 0, 0]

    y, x, dir = horses_info[num]

    if horses_grid[y][x][0] != num:
        return 0

    ny, nx = y + dys[dir], x + dxs[dir]

    if not in_range(ny, nx) or grid[ny][nx] == 2:
        next_dir = change_dir(dir)
        horses_info[num][2] = next_dir

        ny, nx = y + dys[next_dir], x + dxs[next_dir]
        if not in_range(ny, nx) or grid[ny][nx] == 2:
            return 0

    if grid[ny][nx] == 1:
        horses_grid[y][x] = reverse_order(horses_grid[y][x])

    push(ny, nx, y, x)
    y, x = ny, nx

    if is_more_four(y, x):
        return 1
    return 0


turn = 1
while turn <= 1000:

    for horse_num in range(K):
        is_terminate = move(horse_num)

        if is_terminate:
            print(turn)
            sys.exit()
    turn += 1
print(-1)

'''
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2
=> -1
'''
'''
4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
1 4 1
=> 1
'''
'''
4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
3 3 3
=> 2
'''
'''
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 3
=> 8
'''
'''
6 10
0 1 2 0 1 1
1 2 0 1 1 0
2 1 0 1 1 0
1 0 1 1 0 2
2 0 1 2 0 1
0 2 1 0 2 1
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
=> 9
'''
