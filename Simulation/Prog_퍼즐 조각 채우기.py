from collections import deque

dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(i, j, table, check):
    puzzle = []
    N = len(table)
    queue = deque()
    queue.append([i, j])
    check[i][j] = True

    while queue:
        y, x = queue.popleft()
        puzzle.append([y, x])

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if not check[ny][nx] and table[ny][nx] == 1:
                    queue.append((ny, nx))
                    check[ny][nx] = True
    return puzzle


def store_puzzle(puzzle_location):
    r_min, r_max = 50, -1
    c_min, c_max = 50, -1

    for location in puzzle_location:
        r, c = location
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)

    r_len = r_max - r_min + 1
    c_len = c_max - c_min + 1

    puzzle = [[0] * c_len for _ in range(r_len)]
    for location in puzzle_location:
        y = location[0] - r_min
        x = location[1] - c_min
        puzzle[y][x] = 1

    return puzzle


def rotation(puzzle):
    N = len(puzzle)
    M = len(puzzle[0])
    result = [[0] * N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            result[c][N - 1 - r] = puzzle[r][c]

    return result


def empty_side(game_board, puzzle, i, j):
    N = len(game_board)
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == 1:
                for dy, dx in zip(dys, dxs):
                    ny, nx = y + i + dy, x + j + dx
                    if 0 <= ny < N and 0 <= nx < N:
                        if game_board[ny][nx] != 1:
                            return True

    return False


def is_match(puzzle, game_board):
    N = len(game_board)
    R = len(puzzle)
    C = len(puzzle[0])
    for i in range(N - R + 1):
        for j in range(N - C + 1):
            match = True
            for y in range(len(puzzle)):
                for x in range(len(puzzle[0])):
                    game_board[y + i][x + j] += puzzle[y][x]
                    if game_board[y + i][x + j] != 1:
                        match = False

            if empty_side(game_board, puzzle, i, j):
                match = False

            if match:
                return True
            else:
                for y in range(len(puzzle)):
                    for x in range(len(puzzle[0])):
                        game_board[y + i][x + j] -= puzzle[y][x]

    return False


def solution(game_board, table):
    N = len(game_board)
    puzzles = []
    check = [[False] * N for _ in range(N)]
    puzzle_sum = []

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not check[i][j]:
                puzzle_location = bfs(i, j, table, check)
                puzzle = store_puzzle(puzzle_location)
                puzzles.append(puzzle)
                puzzle_sum.append(len(puzzle_location))

    answer = 0
    for idx, puzzle in enumerate(puzzles):
        for _ in range(4):
            puzzle = rotation(puzzle)
            if is_match(puzzle, game_board):
                answer += puzzle_sum[idx]
                break

    return answer
