EMPTY_SMELL = (401, 401)
EMPTY_SHARK = 401


def init():
    n, m, k = tuple(map(int, input().split()))
    shark = [list(map(int, input().split())) for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if shark[r][c] == 0:
                shark[r][c] = EMPTY_SHARK

    shark_cur_dir = [0] + list(map(int, input().split()))
    shark_priority = dict()

    for shark_num in range(1, m + 1):
        shark_priority[shark_num] = list()
        shark_priority[shark_num].append([0, 0, 0, 0])
        for _ in range(4):
            shark_priority[shark_num].append(list(map(int, input().split())))
    return n, m, k, shark, shark_cur_dir, shark_priority


def spray_smell():
    for r in range(N):
        for c in range(N):
            if shark[r][c] != EMPTY_SHARK:
                smell[r][c] = (shark[r][c], K)


def initialize_next_shark():
    global next_shark
    for r in range(N):
        for c in range(N):
            next_shark[r][c] = EMPTY_SHARK


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def move(shark_num, shark_r, shark_c):
    # 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
    delta = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    dir = shark_cur_dir[shark_num]
    priority = shark_priority[shark_num][dir]

    for changed_dir in priority:
        next_r, next_c = shark_r + delta[changed_dir][0], shark_c + delta[changed_dir][1]
        if in_range(next_r, next_c) and smell[next_r][next_c] == EMPTY_SMELL:
            shark_cur_dir[shark_num] = changed_dir
            if shark_num < next_shark[next_r][next_c]:
                next_shark[next_r][next_c] = shark_num
            return

    for changed_dir in priority:
        next_r, next_c = shark_r + delta[changed_dir][0], shark_c + delta[changed_dir][1]
        if in_range(next_r, next_c) and smell[next_r][next_c][0] == shark_num:
            shark_cur_dir[shark_num] = changed_dir
            if shark_num < next_shark[next_r][next_c]:
                next_shark[next_r][next_c] = shark_num
            return

    next_shark[shark_r][shark_c] = shark_num


def move_sharks():
    global next_shark
    initialize_next_shark()

    for r in range(N):
        for c in range(N):
            if shark[r][c] != EMPTY_SHARK:
                move(shark[r][c], r, c)

    for r in range(N):
        for c in range(N):
            shark[r][c] = next_shark[r][c]


def discount_smell():
    for r in range(N):
        for c in range(N):
            if smell[r][c] != EMPTY_SMELL:
                shark_num, smell_persistence = smell[r][c]
                smell_persistence -= 1
                if smell_persistence == 0:
                    smell[r][c] = EMPTY_SMELL
                else:
                    smell[r][c] = (shark_num, smell_persistence)


def is_only_one():
    for r in range(N):
        for c in range(N):
            if 1 < shark[r][c] < 401:
                return False
    return True


N, M, K, shark, shark_cur_dir, shark_priority = init()
smell = [[(401, 401)] * N for _ in range(N)]
next_shark = [[401] * N for _ in range(N)]

elapsed_time = 0

while True:
    if elapsed_time >= 1000:
        print(-1)
        break

    spray_smell()
    move_sharks()
    discount_smell()

    elapsed_time += 1
    if is_only_one():
        print(elapsed_time)
        break


'''
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
'''
