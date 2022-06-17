def init():
    grid = [list(input().strip()) for _ in range(R)]
    orders = list(input().strip())

    destination = []
    current_pos = (0, 0)
    current_box_count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '+':
                destination.append((i, j))
            elif grid[i][j] == 'w':
                current_pos = (i, j)
                grid[i][j] = '.'
            elif grid[i][j] == 'W':
                current_pos = (i, j)
                destination.append((i, j))
                grid[i][j] = '+'
            elif grid[i][j] == 'B':
                current_box_count += 1
                destination.append((i, j))
    total_box_count = len(destination)

    return grid, orders, destination, current_pos, current_box_count, total_box_count


def simulate():
    global current_box_count

    y, x = current_pos
    for order in orders:
        if current_box_count == total_box_count:
            break

        ny, nx = y + direction[order][0], x + direction[order][1]

        if grid[ny][nx] in '.+':
              y, x = ny, nx
        elif grid[ny][nx] in 'bB':
            nny, nnx = ny + direction[order][0], nx + direction[order][1]
            if grid[nny][nnx] in '.+':
                if grid[nny][nnx] == '+':
                    current_box_count += 1
                grid[ny][nx], grid[nny][nnx] = '.', 'b'
                if (ny, nx) in destination:
                    grid[ny][nx] = '+'
                    current_box_count -= 1
                y, x = ny, nx

    grid[y][x] = 'w'
    return current_box_count


def print_game_result():
    if current_box_count == total_box_count:
        result = 'complete'
    else:
        result = 'incomplete'
    print("Game %d: %s" % (test_case, result))


def print_game_status():
    for y in range(R):
        for x in range(C):
            if (y, x) in destination and grid[y][x].isalpha():
                print(grid[y][x].upper(), end='')
            else:
                print(grid[y][x], end='')
        print()


test_case = 1
direction = {
        'U': [-1, 0],
        'D': [1, 0],
        'L': [0, -1],
        'R': [0, 1]
}

while True:
    R, C = tuple(map(int, input().split()))
    if (R, C) == (0, 0):
        break
    grid, orders, destination, current_pos, current_box_count, total_box_count = init()
    current_box_count = simulate()
    print_game_result()
    print_game_status()
    test_case += 1

'''
8 9
#########
#...#...#
#..bb.b.#
#...#w#.#
#...#b#.#
#...++++#
#...#..##
#########
ULRURDDDUULLDDD
6 7
#######
#..####
#.+.+.#
#.bb#w#
##....#
#######
DLLUDLULUURDRDDLUDRR
0 0
'''
