def init():
    N, K = tuple(map(int, input().split()))
    A = list(map(int, input().split()))
    return N, K, A


def rotate_belt():
    temp_durability = belt_durability[0][0]
    temp_robot = belt_robot[0][0]

    start_row, start_col = 0, 0
    end_row, end_col = 1, N - 1

    for row in range(start_row, end_row):
        belt_durability[row][start_col] = belt_durability[row + 1][start_col]
        belt_robot[row][start_col] = belt_robot[row + 1][start_col]

    for col in range(start_col, end_col):
        belt_durability[end_row][col] = belt_durability[end_row][col + 1]
        belt_robot[end_row][col] = belt_robot[end_row][col + 1]

    for row in range(end_row, start_row, -1):
        belt_durability[row][end_col] = belt_durability[row - 1][end_col]
        belt_robot[row][end_col] = belt_robot[row - 1][end_col]

    for col in range(end_col, start_col, -1):
        belt_durability[start_row][col] = belt_durability[start_row][col - 1]
        belt_robot[start_row][col] = belt_robot[start_row][col - 1]

    belt_durability[start_row][start_col + 1] = temp_durability
    belt_robot[start_row][start_col + 1] = temp_robot

    if belt_robot[0][N - 1]:
        belt_robot[0][N - 1] = 0


def move_robot():
    r = 0
    for c in range(N - 2, -1, -1):
        if belt_robot[r][c]:
            next_r, next_c = r + drs[0], c + dcs[0]
            if belt_robot[next_r][next_c] == 0 and belt_durability[next_r][next_c] >= 1:
                belt_robot[next_r][next_c] = belt_robot[r][c]
                belt_robot[r][c] = 0
                belt_durability[next_r][next_c] -= 1

    if belt_robot[0][N - 1]:
        belt_robot[0][N - 1] = 0


def put_robot():
    global total_robot_cnt
    if belt_durability[0][0] != 0:
        total_robot_cnt += 1
        belt_robot[0][0] = total_robot_cnt
        belt_durability[0][0] -= 1


def is_end():
    count = 0
    for r in range(2):
        for c in range(N):
            if belt_durability[r][c] == 0:
                count += 1
    return count >= K


def print_belt_durability():
    for r in range(2):
        for c in range(N):
            print(belt_durability[r][c], end=" ")
        print()


def print_belt_robot():
    for r in range(2):
        for c in range(N):
            print(belt_robot[r][c], end=" ")
        print()


level = 1
N, K, A = init()

belt_durability = [[0] * N for _ in range(2)]
belt_durability[0] = A[0:N]
belt_durability[1] = list(reversed(A[N:2 * N]))
belt_robot = [[0] * N for _ in range(2)]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

total_robot_cnt = 0

while True:
    rotate_belt()
    move_robot()
    put_robot()

    if is_end():
        break
    level += 1

print(level)


'''
3 2
1 2 1 2 1 2
'''
'''
3 6
10 10 10 10 10 10
'''
'''
4 5
10 1 10 6 3 4 8 2
'''
'''
5 8
100 99 60 80 30 20 10 89 99 100
'''
'''
7 7
7 4 4 3 2 6 9 7 5 2 1 2 3 8 
'''
