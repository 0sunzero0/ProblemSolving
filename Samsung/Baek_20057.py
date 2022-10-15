sand_ratio = [
            [
                [0, 0, 2, 0, 0],
                [0, 10, 7, 1, 0],
                [5, 0, 0, 0, 0],
                [0, 10, 7, 1, 0],
                [0, 0, 2, 0, 0]
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [2, 7, 0, 7, 2],
                [0, 10, 0, 10, 0],
                [0, 0, 5, 0, 0]
            ],
            [
                [0, 0, 2, 0, 0],
                [0, 1, 7, 10, 0],
                [0, 0, 0, 0, 5],
                [0, 1, 7, 10, 0],
                [0, 0, 2, 0, 0]
            ],
            [
                [0, 0, 5, 0, 0],
                [0, 10, 0, 10, 0],
                [2, 7, 0, 7, 2],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0]
            ]
]


def init():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    return N, grid


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def spread(r, c, d):
    global answer

    sand = grid[r][c]

    # y에서 비율만큼 새로운 칸에 추가하기
    for i in range(spread_size):
        for j in range(spread_size):
            next_r, next_c = r - 2 + i,  c - 2 + j
            if in_range(next_r, next_c):
                grid[next_r][next_c] += sand * (sand_ratio[d][i][j]) // 100
                grid[r][c] -= sand * (sand_ratio[d][i][j]) // 100
            else:
                answer += sand * (sand_ratio[d][i][j]) // 100
                grid[r][c] -= sand * (sand_ratio[d][i][j]) // 100

    # 남은 y를 a에 보내기
    next_r, next_c = r + drs[d], c + dcs[d]
    if in_range(next_r, next_c):
        grid[next_r][next_c] += grid[r][c]
        grid[r][c] = 0
    else:
        answer += grid[r][c]
        grid[r][c] = 0


def simulate():
    cur_r, cur_c = N // 2, N // 2
    cur_d = 0
    move_step = 1

    while 0 <= cur_r < N and 0 <= cur_c < N:
        for _ in range(move_step):
            cur_r += drs[cur_d]
            cur_c += dcs[cur_d]

            spread(cur_r, cur_c, cur_d)

        cur_d = (cur_d + 1) % 4
        if cur_d == 0 or cur_d == 2:
            move_step += 1


drs = [0, 1, 0, -1]
dcs = [-1, 0, 1, 0]
spread_size = 5
answer = 0

N, grid = init()
simulate()

print(answer)

'''
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0
'''
'''
7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 0 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
'''
'''
9
193 483 223 482 858 274 847 283 748
484 273 585 868 271 444 584 293 858
828 384 382 818 347 858 293 999 727
818 384 727 373 636 141 234 589 991
913 564 555 827 0 999 123 123 123
321 321 321 983 982 981 983 980 990
908 105 270 173 147 148 850 992 113
943 923 982 981 223 131 222 913 562
752 572 719 590 551 179 141 137 731
'''
