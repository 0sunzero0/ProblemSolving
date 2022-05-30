import sys

input = sys.stdin.readline
sys.setrecursionlimit(500 * 500)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]


def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


def go(y, x):
    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1

    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if in_range(ny, nx):
            if graph[ny][nx] > graph[y][x]:
                dp[y][x] = max(dp[y][x], go(ny, nx) + 1)

    return dp[y][x]


for y in range(N):
    for x in range(N):
        go(y, x)

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dp[i][j])
print(answer)

'''
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
'''
