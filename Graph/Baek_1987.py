R, C = tuple(map(int, input().split()))
board = [ list(map(lambda x : ord(x) - 65, input().rstrip())) for _ in range(R) ]
visited = [False] * 26
max_count = 1


def in_range(y, x):
    return 0 <= y < R and 0 <= x < C


def can_go(y, x):
    return in_range(y, x) and not visited[board[y][x]]


def dfs(y, x, count):
    global max_count

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if can_go(ny, nx):
            visited[board[ny][nx]] = True
            dfs(ny, nx, count + 1)
            visited[board[ny][nx]] = False

    max_count = max(count, max_count)


visited[board[0][0]] = True
dfs(0, 0, 1)
print(max_count)

'''
2 4
CAAB
ADCB
'''
