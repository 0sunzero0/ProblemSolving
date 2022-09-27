def init():
    r, c, k = tuple(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(3)]

    grid = [[0] * 100 for _ in range(100)]
    for i in range(3):
        for j in range(3):
            grid[i][j] = a[i][j]

    return r - 1, c - 1, k, grid


def in_range(i, j):
    return 0 <= i < cur_row_num and 0 <= j < cur_col_num


def calculate_r():
    global cur_col_num
    next_grid = [[0] * 100 for _ in range(100)]

    new_col_num = 0
    for row in range(cur_row_num):
        count = dict()

        for col in range(cur_col_num):
            if grid[row][col] == 0:
                continue

            if grid[row][col] in count:
                count[grid[row][col]] += 1
            else:
                count[grid[row][col]] = 1

        sorted_count = sorted(count.items(), key=lambda x: (x[1], x[0]))
        col = 0
        for key, value in sorted_count:
            next_grid[row][col * 2], next_grid[row][col * 2 + 1] = key, value
            col += 1
            new_col_num = max(new_col_num, col * 2)

    cur_col_num = new_col_num

    for i in range(cur_row_num):
        for j in range(cur_col_num):
            grid[i][j] = next_grid[i][j]


def calculate_c():
    global cur_row_num
    next_grid = [[0] * 100 for _ in range(100)]

    new_row_num = 0
    for col in range(cur_col_num):
        count = dict()

        for row in range(cur_row_num):
            if grid[row][col] == 0:
                continue

            if grid[row][col] in count:
                count[grid[row][col]] += 1
            else:
                count[grid[row][col]] = 1

        sorted_count = sorted(count.items(), key=lambda x: (x[1], x[0]))
        row = 0
        for key, value in sorted_count:
            next_grid[row * 2][col], next_grid[row * 2 + 1][col] = key, value
            row += 1
            new_row_num = max(new_row_num, row * 2)

    cur_row_num = new_row_num

    for i in range(cur_row_num):
        for j in range(cur_col_num):
            grid[i][j] = next_grid[i][j]


def simulate():
    if cur_row_num >= cur_col_num:
        calculate_r()
    else:
        calculate_c()


def print_grid():
    for i in range(cur_row_num):
        for j in range(cur_col_num):
            print(grid[i][j], end=" ")
        print()
    print()


r, c, k, grid = init()
cur_row_num, cur_col_num = 3, 3
time = 0

while True:
    if in_range(r, c) and grid[r][c] == k:
        print(time)
        break
    if time > 100:
        print(-1)
        break
    simulate()
    # print_grid()
    time += 1

'''
1 2 2
1 2 1
2 1 3
3 3 3
'''
'''
1 2 1
1 2 1
2 1 3
3 3 3
'''
'''
1 2 3
1 2 1
2 1 3
3 3 3
'''
'''
1 2 4
1 2 1
2 1 3
3 3 3
'''
