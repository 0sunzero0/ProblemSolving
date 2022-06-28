import sys

N = 9
sudoku = [list(map(int, input().split())) for _ in range(N)]
check1 = [[False] * 10 for _ in range(N)]
check2 = [[False] * 10 for _ in range(N)]
check3 = [[False] * 10 for _ in range(N)]
blank = []


def coord_to_square(y, x):
    return (y // 3) * 3 + (x // 3)


def is_sudoku():
    for i in range(N):
        for j in range(N):
            num = sudoku[i][j]
            if not (check1[i][num] and check2[j][num] and check3[coord_to_square(i, j)][num]):
                return False
    return True


def print_sudoku():
    for i in range(N):
        for j in range(N):
            print(sudoku[i][j], end=" ")
        print()


def can_put(y, x, num):
    return not check1[y][num] and not check2[x][num] and not check3[coord_to_square(y, x)][num]


def go(curr_idx):
    if curr_idx == len(blank):
        if is_sudoku():
            print_sudoku()
            sys.exit(0)
        return

    y, x = blank[curr_idx]
    for num in range(1, N + 1):
        if can_put(y, x, num):
            sudoku[y][x] = num
            check1[y][num] = check2[x][num] = check3[coord_to_square(y, x)][num] = True
            go(curr_idx + 1)
            sudoku[y][x] = 0
            check1[y][num] = check2[x][num] = check3[coord_to_square(y, x)][num] = False


for i in range(N):
    for j in range(N):
        if sudoku[i][j] != 0:
            check1[i][sudoku[i][j]] = True
            check2[j][sudoku[i][j]] = True
            check3[coord_to_square(i, j)][sudoku[i][j]] = True
        else:
            blank.append((i, j))

go(0)

'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
'''
