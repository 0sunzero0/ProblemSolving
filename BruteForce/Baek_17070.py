HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2


def go(cur_r, cur_c, status):
    global answer

    if (cur_r, cur_c) == end:
        answer += 1
        return

    if status == HORIZONTAL or status == DIAGONAL:
        cur_dir = HORIZONTAL
        if cur_c + 1 < N and grid[cur_r][cur_c + 1] == 0:
            go(cur_r, cur_c + 1, cur_dir)

    if status == VERTICAL or status == DIAGONAL:
        cur_dir = VERTICAL
        if cur_r + 1 < N and grid[cur_r + 1][cur_c] == 0:
            go(cur_r + 1, cur_c, cur_dir)

    if cur_r + 1 < N and cur_c + 1 < N and \
       grid[cur_r][cur_c + 1] == 0 and grid[cur_r + 1][cur_c] == 0 and grid[cur_r + 1][cur_c + 1] == 0:
        cur_dir = DIAGONAL
        go(cur_r + 1, cur_c + 1, cur_dir)


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

start = (0, 0)
end = (N - 1, N - 1)

answer = 0
go(0, 1, HORIZONTAL)
print(answer)
