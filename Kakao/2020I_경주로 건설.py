from collections import deque


def is_corner(cdir, ndir):
    if cdir % 2 == ndir % 2:
        return False
    return True


def in_range(y, x, N):
    return 0 <= y < N and 0 <= x < N


def can_go(y, x, board):
    return in_range(y, x, len(board)) and board[y][x] == 0


def solution(board):
    N = len(board)
    MAX_INT = 500 * 500 * 25 * 25
    visited = [[[MAX_INT] * 4 for _ in range(N)] for _ in range(N)]
    dys, dxs = [-1, 0, 1, 0], [0, -1, 0, 1]

    queue = deque()
    for dir in (2, 3):
        queue.append((0, 0, 0, dir))
        visited[0][0][dir] = 0

    while queue:
        cost, y, x, cdir = queue.popleft()

        for ndir in range(4):
            ny, nx = y + dys[ndir], x + dxs[ndir]
            if can_go(ny, nx, board):
                ncost = cost + 100
                if is_corner(cdir, ndir):
                    ncost += 500
                if ncost < visited[ny][nx][ndir]:
                    visited[ny][nx][ndir] = ncost
                    queue.append((ncost, ny, nx, ndir))

    return min(visited[N - 1][N - 1])
