def rotate(arr):
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = arr[i][j]
    return result


def check(new_lock):
    origin_lock_len = len(new_lock) // 3
    for i in range(origin_lock_len, origin_lock_len * 2):
        for j in range(origin_lock_len, origin_lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for r in range(n * 2):
            for c in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[r + i][c + j] += key[i][j]

                if check(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[r + i][c + j] -= key[i][j]

    return False
