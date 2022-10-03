def init():
    n, m, k = tuple(map(int, input().split()))
    input_grid = [
        [list() for _ in range(n)]
        for _ in range(n)
    ]

    for _ in range(m):
        r, c, m, s, d = tuple(map(int, input().split()))
        input_grid[r - 1][c - 1].append((m, s, d))

    return n, m, k, input_grid


def get_next(r, c, speed, move_dir):
    drs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dcs = [0, 1, 1, 1, 0, -1, -1, -1]

    next_r = (r + drs[move_dir] * speed + N * speed) % N
    next_c = (c + dcs[move_dir] * speed + N * speed) % N

    return next_r, next_c


def move_fireball(cur_r, cur_c, mass, speed, move_dir):
    next_r, next_c = get_next(cur_r, cur_c, speed, move_dir)
    next_grid[next_r][next_c].append((mass, speed, move_dir))


def move():
    for r in range(N):
        for c in range(N):
            for element in grid[r][c]:
                m, s, d = element
                move_fireball(r, c, m, s, d)


def split(r, c):
    sum_of_mass, sum_of_speed, fireball_cnt = 0, 0, len(next_grid[r][c])
    num_of_dir_type = [0, 0]

    for mass, speed, move_dir in next_grid[r][c]:
        sum_of_mass += mass
        sum_of_speed += speed
        num_of_dir_type[move_dir % 2] += 1

    if not num_of_dir_type[0] or not num_of_dir_type[1]:
        next_directions = [0, 2, 4, 6]
    else:
        next_directions = [1, 3, 5, 7]

    next_mass = sum_of_mass // 5
    next_speed = sum_of_speed // fireball_cnt

    for move_dir in next_directions:
        if next_mass > 0:
            grid[r][c].append((next_mass, next_speed, move_dir))


def compound():
    for r in range(N):
        for c in range(N):
            grid[r][c] = list()

    for r in range(N):
        for c in range(N):
            fireball_cnt = len(next_grid[r][c])
            if fireball_cnt >= 2:
                split(r, c)
            elif fireball_cnt == 1:
                for element in next_grid[r][c]:
                    grid[r][c].append(element)


def get_answer():
    result = 0
    for r in range(N):
        for c in range(N):
            for element in grid[r][c]:
                m, s, d = element
                result += m
    return result


def print_grid():
    for r in range(N):
        for c in range(N):
            print(grid[r][c], end=" ")
        print()
    print()


def print_next_grid():
    for r in range(N):
        for c in range(N):
            print(next_grid[r][c], end=" ")
        print()
    print()


N, M, K, grid = init()
next_grid = [
    [list() for _ in range(N)]
    for _ in range(N)
]

for _ in range(K):
    for r in range(N):
        for c in range(N):
            next_grid[r][c] = list()
    move()
    compound()

print(get_answer())

'''
4 2 1
1 1 5 2 2
1 4 7 1 6
'''
'''
4 2 2
1 1 5 2 2
1 4 7 1 6
'''
