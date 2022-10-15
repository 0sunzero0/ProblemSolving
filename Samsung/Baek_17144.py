def init():
    R, C, T = tuple(map(int, input().split()))
    room = [list(map(int, input().split())) for _ in range(R)]
    return R, C, T, room


def get_cleaner_pos():
    for r in range(R):
        if room[r][0] == -1:
            cleaner_up_pos = (r, 0)
            break
    cleaner_down_pos = (r + 1, 0)
    return cleaner_up_pos, cleaner_down_pos


def not_cleaner(r, c):
    return room[r][c] != -1


def in_range(r, c):
    return 0 <= r < R and 0 <= c < C


def spread():
    drs = [-1, 0, 1, 0]
    dcs = [0, -1, 0, 1]
    next_room = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if not_cleaner(r, c):
                for dr, dc in zip(drs, dcs):
                    nr, nc = r + dr, c + dc
                    if in_range(nr, nc) and not_cleaner(nr, nc):
                        next_room[nr][nc] += room[r][c] // 5
                        next_room[r][c] -= room[r][c] // 5

    for r in range(R):
        for c in range(C):
            room[r][c] += next_room[r][c]


def rotate_counter_clockwise(start_row, start_col, end_row, end_col):
    temp = room[start_row][start_col]
    for col in range(start_col, end_col):
        room[start_row][col] = room[start_row][col + 1]
    for row in range(start_row, end_row):
        room[row][end_col] = room[row + 1][end_col]
    for col in range(end_col, start_col, -1):
        room[end_row][col] = room[end_row][col - 1]
    for row in range(end_row, start_row, -1):
        room[row][start_col] = room[row - 1][start_col]
    room[start_row + 1][start_col] = temp


def rotate_clockwise(start_row, start_col, end_row, end_col):
    temp = room[start_row][start_col]
    for row in range(start_row, end_row):
        room[row][start_col] = room[row + 1][start_col]
    for col in range(start_col, end_col):
        room[end_row][col] = room[end_row][col + 1]
    for row in range(end_row, start_row, -1):
        room[row][end_col] = room[row - 1][end_col]
    for col in range(end_col, start_col, -1):
        room[start_row][col] = room[start_row][col - 1]
    room[start_row][start_col + 1] = temp


def simulate():
    cleaner_up_pos, cleaner_down_pos = get_cleaner_pos()
    # 1. 미세먼지가 확산
    spread()
    # 2. 공기청정기가 작동
    # 2-1. 위쪽 공기청정기의 바람은 반시계방향으로 순환
    rotate_counter_clockwise(0, 0, cleaner_up_pos[0], C - 1)
    # 2-2. 아래쪽 공기청정기의 바람은 시계방향으로 순환
    rotate_clockwise(cleaner_down_pos[0], 0, R - 1, C - 1)
    # 3. 공기청정기로 들어간 미세먼지는 모두 정화
    room[cleaner_up_pos[0]][0] = room[cleaner_down_pos[0]][0] = -1
    room[cleaner_up_pos[0]][1] = room[cleaner_down_pos[0]][1] = 0


def get_answer():
    answer = 0
    for r in range(R):
        for c in range(C):
            if room[r][c] != -1:
                answer += room[r][c]
    return answer


R, C, T, room = init()
for _ in range(T):
    simulate()
print(get_answer())

'''
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''
