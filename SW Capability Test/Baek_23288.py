from collections import deque

CLOCKWISE = True
EAST, SOUTH, WEST, NORTH = 0, 1, 2, 3


def init():
    N, M, K = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    return N, M, K, grid


def roll(d):
    global cur_r, cur_c
    next_dice = dict()
    if d == EAST:
        next_dice["front"] = dice["front"]
        next_dice["down"] = dice["right"]
        next_dice["right"] = 7 - dice["down"]
        cur_c += 1
    elif d == SOUTH:
        next_dice["front"] = 7 - dice["down"]
        next_dice["down"] = dice["front"]
        next_dice["right"] = dice["right"]
        cur_r += 1
    elif d == WEST:
        next_dice["front"] = dice["front"]
        next_dice["down"] = 7 - dice["right"]
        next_dice["right"] = dice["down"]
        cur_c -= 1
    elif d == NORTH:
        next_dice["front"] = dice["down"]
        next_dice["down"] = 7 - dice["front"]
        next_dice["right"] = dice["right"]
        cur_r -= 1

    return next_dice


def score(start_r, start_c):
    visit = [[False] * M for _ in range(N)]
    score_queue = deque()
    target = grid[start_r][start_c]

    count = 1
    visit[start_r][start_c] = True
    score_queue.append((start_r, start_c))

    while score_queue:
        r, c = score_queue.popleft()
        for dr, dc in zip(drs, dcs):
            next_r, next_c = r + dr, c + dc
            if in_range(next_r, next_c):
                if grid[next_r][next_c] == target and not visit[next_r][next_c]:
                    count += 1
                    visit[next_r][next_c] = True
                    score_queue.append((next_r, next_c))

    return target * count


def rotate_dir(d, is_clockwise):
    if is_clockwise:
        return (d + 1) % 4
    return (d - 1) % 4


def change_dir(d):
    return (d + 2) % 4


def in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def simulate():
    global total_score, dice, cur_dir

    next_r, next_c = cur_r + drs[cur_dir], cur_c + dcs[cur_dir]
    if not in_range(next_r, next_c):
        cur_dir = change_dir(cur_dir)

    dice = roll(cur_dir)

    total_score += score(cur_r, cur_c)

    if dice["down"] > grid[cur_r][cur_c]:
        cur_dir = rotate_dir(cur_dir, CLOCKWISE)
    elif dice["down"] < grid[cur_r][cur_c]:
        cur_dir = rotate_dir(cur_dir, not CLOCKWISE)


dice = {"front": 5, "right": 3, "down": 6}
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

N, M, K, grid = init()
cur_dir, cur_r, cur_c = EAST, 0, 0
total_score = 0

for _ in range(K):
    simulate()

print(total_score)

'''
4 5 3
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
'''
'''
4 5 1000
4 1 2 3 3
6 1 1 3 3
5 6 1 3 2
5 5 6 5 5
'''
