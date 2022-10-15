NOT_ROTATE = 0
CW = 1
ACW = -1


def init():
    gear = [[0] * m for _ in range(n + 1)]
    for i in range(1, n + 1):
        given_row = list(map(int, input()))
        for j, elem in enumerate(given_row):
            gear[i][j] = elem
    k = int(input())
    rotate_infos = [tuple(map(int, input().split())) for _ in range(k)]
    return gear, k, rotate_infos


def shift(row, direction):
    if direction == CW:
        temp = gear[row][m - 1]
        for col in range(m - 1, 0, -1):
            gear[row][col] = gear[row][col - 1]
        gear[row][0] = temp
    elif direction == ACW:
        temp = gear[row][0]
        for col in range(m - 1):
            gear[row][col] = gear[row][col + 1]
        gear[row][m - 1] = temp


def rotate(rotate_dir):
    for gear_num in range(1, n + 1):
        shift(gear_num, rotate_dir[gear_num])


def flip(standard_dir):
    return standard_dir * -1


def simulate(start_num, start_dir):
    rotate_dir = [NOT_ROTATE for _ in range(n + 1)]
    rotate_dir[start_num] = start_dir

    for i in range(start_num - 1, 0, -1):
        if gear[i][2] != gear[i + 1][6]:
            rotate_dir[i] = flip(rotate_dir[i + 1])
        else:
            break

    for i in range(start_num + 1, n + 1):
        if gear[i][6] != gear[i - 1][2]:
            rotate_dir[i] = flip(rotate_dir[i - 1])
        else:
            break

    rotate(rotate_dir)


def pro():
    for start_num, start_dir in rotate_infos:
        simulate(start_num, start_dir)


def print_answer():
    print(gear[1][0] + gear[2][0] * 2 + gear[3][0] * 4 + gear[4][0] * 8)


n, m = 4, 8
gear, k, rotate_infos = init()
pro()
print_answer()

'''
10101111
01111101
11001110
00000010
2
3 -1
1 1
'''
'''
11111111
11111111
11111111
11111111
3
1 1
2 1
3 1
'''
