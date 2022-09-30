BLUE = 2
RED = 1
WHITE = 0


def init():
    n, k = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(n)]
    horse_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]

    for horse_num in range(1, k + 1):
        horse_r, horse_c, horse_dir = tuple(map(int, input().split()))
        horse_r, horse_c = horse_r - 1, horse_c - 1
        horse_grid[horse_r][horse_c].append((horse_num, horse_dir))

    return n, k, grid, horse_grid


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def pop_horses(target_num, target_r, target_c):
    for i, (horse_num, _) in enumerate(horse_grid[target_r][target_c]):
        if horse_num == target_num:
            horses = horse_grid[target_r][target_c][i:]
            del horse_grid[target_r][target_c][i:]
            return horses


def transpose_dir(cur_dir):
    if cur_dir == 1:
        return 2
    elif cur_dir == 2:
        return 1
    elif cur_dir == 3:
        return 4
    elif cur_dir == 4:
        return 3


def move(cur_horse_num, cur_r, cur_c, cur_dir):
    next_r, next_c = cur_r + dr[cur_dir], cur_c + dc[cur_dir]
    need_reverse = False
    is_more_four = False

    if not in_range(next_r, next_c) or grid[next_r][next_c] == BLUE:
        cur_dir = transpose_dir(cur_dir)
        next_r, next_c = cur_r + dr[cur_dir], cur_c + dc[cur_dir]

        if not in_range(next_r, next_c) or grid[next_r][next_c] == BLUE:
            next_r, next_c = cur_r, cur_c
        elif grid[next_r][next_c] == RED:
            need_reverse = True

    elif grid[next_r][next_c] == RED:
        need_reverse = True

    to_move = pop_horses(cur_horse_num, cur_r, cur_c)
    to_move[0] = (cur_horse_num, cur_dir)

    if need_reverse:
        to_move.reverse()

    horse_grid[next_r][next_c].extend(to_move)

    if len(horse_grid[next_r][next_c]) >= 4:
        is_more_four = True
    return is_more_four


def find_horse_num(target_num):
    for r in range(N):
        for c in range(N):
            for horse_num, horse_dir in horse_grid[r][c]:
                if horse_num == target_num:
                    return horse_num, r, c, horse_dir


def simulate():
    for target_num in range(1, K + 1):
        horse_num, r, c, horse_dir = find_horse_num(target_num)
        is_more_four = move(horse_num, r, c, horse_dir)

        if is_more_four:
            return True

    return False


def print_horse_grid():
    for i in range(N):
        for j in range(N):
            print(horse_grid[i][j], end=" ")
        print()
    print()


N, K, grid, horse_grid = init()

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
turn = 0

# print_horse_grid()
while True:
    if turn > 1000:
        print(-1)
        break

    turn += 1
    if simulate():
        # print_horse_grid()
        print(turn)
        break
    # print_horse_grid()

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
2 4 3
'''
