N, M = tuple(map(int, input().split()))
grid = [ input().rstrip() for _ in range(N) ]
min_count = 11


def get_start_pos():
    coin_pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'o':
                coin_pos.append((i, j))

    return coin_pos


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x):
    if 0 <= y < N and 0 <= x < M:
        return not grid[y][x] == '#'
    return True


def go(y1, x1, y2, x2, count):
    global min_count

    if not in_range(y1, x1) and not in_range(y2, x2):
        return
    elif not in_range(y1, x1) or not in_range(y2, x2):
        min_count = min(min_count, count)
        return

    if count > 10:
        return

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    for dy, dx in zip(dys, dxs):
        ny1, nx1 = y1 + dy, x1 + dx
        ny2, nx2 = y2 + dy, x2 + dx
        if can_go(ny1, nx1) and can_go(ny2, nx2):
            go(ny1, nx1, ny2, nx2, count + 1)
        elif can_go(ny1, nx1):
            go(ny1, nx1, y2, x2, count + 1)
        elif can_go(ny2, nx2):
            go(y1, x1, ny2, nx2, count + 1)


coin1_start_pos, coin2_start_pos = get_start_pos()
go(coin1_start_pos[0], coin1_start_pos[1], coin2_start_pos[0], coin2_start_pos[1], 0)

if min_count == 11:
    print(-1)
else:
    print(min_count)

'''
1 2
oo
'''
'''
6 2
..
..
..
o#
o#
##
'''
