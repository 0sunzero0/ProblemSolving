N, M = tuple(map(int, input().split()))
game_board = [input() for _ in range(N)]
check = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_go(y, x, color):
    return in_range(y, x) and game_board[y][x] == color


def go(y, x, count, color):
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

    if check[y][x]:
        if count - dist[y][x] >= 4:
            return True
        else:
            return False

    check[y][x] = True
    dist[y][x] = count

    for idx in range(4):
        ny, nx = y + dys[idx], x + dxs[idx]
        if can_go(ny, nx, color):
            if go(ny, nx, count + 1, color):
                return True

    return False


for i in range(N):
    for j in range(M):
        if check[i][j]:
            continue

        dist = [[0] * M for _ in range(N)]
        is_cycle = go(i, j, 1, game_board[i][j])

        if is_cycle:
            print('Yes')
            exit()

print('No')

'''
3 4
AAAA
ABCA
AAAA
'''
