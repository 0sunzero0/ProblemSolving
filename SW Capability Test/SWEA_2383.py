from collections import deque


def init():
    n = int(input())
    input_grid = [list(map(int, input().split())) for _ in range(n)]
    return n, input_grid


def get_p_pos():
    result = list()
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                result.append((i, j))
    return result


def get_s_pos():
    result = list()
    value = list()
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2:
                result.append((i, j))
                value.append(grid[i][j])
    return value[0], value[1], result


def get_dist_to_stair(person_pos, num):
    pr, pc = person_pos
    sr, sc = stairs_pos[num - 1]
    return abs(pr - sr) + abs(pc - sc)


def move_people():
    cur_time = 0

    one_queue = list()
    two_queue = list()

    for idx, pos in enumerate(people_pos):
        if idx in one_stair_idx:
            one_queue.append((idx, get_dist_to_stair(pos, 1)))
        else:
            two_queue.append((idx, get_dist_to_stair(pos, 2)))

    one_queue.sort(key=lambda x: x[1])
    two_queue.sort(key=lambda x: x[1])

    one_queue = deque(one_queue)
    two_queue = deque(two_queue)

    first_stair = deque()
    second_stair = deque()

    while True:
        if len(one_queue) == 0 and len(two_queue) == 0 and len(first_stair) == 0 and len(second_stair) == 0:
            break

        cur_time += 1

        # 1번 계단에 사람 있으면, 내려가기
        while len(first_stair) != 0:
            if cur_time - first_stair[0] >= first_stair_value:
                first_stair.popleft()
            else:
                break

        # 2번 계단에 사람 있으면, 내려가기
        while len(second_stair) != 0:
            if cur_time - second_stair[0] >= second_stair_value:
                second_stair.popleft()
            else:
                break

        # 1번 계단 처리
        while len(one_queue) != 0:
            idx, time = one_queue[0]
            if time < cur_time and len(first_stair) < 3:
                one_queue.popleft()
                first_stair.append(cur_time)
            else:
                break

        # 2번 계단 처리
        while len(two_queue) != 0:
            idx, time = two_queue[0]
            if time < cur_time and len(second_stair) < 3:
                two_queue.popleft()
                second_stair.append(cur_time)
            else:
                break

    return cur_time


def get_min_time(p_idx):
    global answer

    if p_idx == len(people_pos):
        answer = min(answer, move_people())
        return

    one_stair_idx.add(p_idx)
    get_min_time(p_idx + 1)
    one_stair_idx.remove(p_idx)
    get_min_time(p_idx + 1)


T = int(input())

for test_num in range(1, T + 1):
    N, grid = init()

    people_pos = get_p_pos()
    first_stair_value, second_stair_value, stairs_pos = get_s_pos()
    one_stair_idx = set()

    answer = 10 ** 8
    get_min_time(0)
    print(f"#{test_num} {answer}")

'''
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
'''
'''
10
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
5
0 0 1 1 0
0 0 1 0 2
0 0 0 1 0
0 1 0 0 0
1 0 5 0 0
6
0 0 0 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0
2 0 1 0 0 0
0 0 2 0 0 0
6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 2 0 4
7
0 0 0 0 0 0 0
0 0 0 0 0 0 4
0 0 0 0 1 0 0
1 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 2 0 0 0 0 0
7
0 0 0 0 0 0 0
7 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2 0 0 0 0 1 0
0 0 0 0 0 0 0
8
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 1 0 0 0
8
3 0 0 0 0 0 5 0
0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 1 1 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
9
0 0 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 8
7 0 0 0 0 1 0 0 0
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 0
1 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
3 0 1 0 1 0 0 0 0 2
1 1 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''
