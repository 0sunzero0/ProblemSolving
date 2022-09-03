import sys
sys.setrecursionlimit(500 * 500)

R, C = tuple(map(int, input().split()))
zido = [list(map(int, input().split())) for _ in range(R)]

dp = [[0] * C for _ in range(R)]
dys = [-1, 0, 1, 0]
dxs = [0, -1, 0, 1]
visit = [[False] * C for _ in range(R)]


def in_range(y, x):
    return 0 <= y < R and 0 <= x < C


def go(y, x):
    if y == R - 1 and x == C - 1:
        return 1

    if visit[y][x]:
        return dp[y][x]

    visit[y][x] = True
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if in_range(ny, nx) and zido[ny][nx] < zido[y][x]:
            dp[y][x] += go(ny, nx)

    return dp[y][x]


go(0, 0)
print(dp[0][0])

'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''
