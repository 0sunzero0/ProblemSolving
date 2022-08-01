from itertools import permutations

N, M, K = tuple(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(K)]
answer = 100 * 50


def rotate(r1, c1, r2, c2):
    global arr
    # top
    temp = arr[r1][c2]
    for c in range(c2, c1, -1):
        arr[r1][c] = arr[r1][c - 1]
    # left
    for r in range(r1, r2):
        arr[r][c1] = arr[r + 1][c1]
    # bottom
    for c in range(c1, c2):
        arr[r2][c] = arr[r2][c + 1]
    # right
    for r in range(r2, r1, -1):
        arr[r][c2] = arr[r - 1][c2]
    arr[r1 + 1][c2] = temp


cases = permutations(operations)
for case in cases:
    arr = [[A[r][c] for c in range(M)] for r in range(N)]

    for r, c, size in case:
        r -= 1
        c -= 1

        for s in range(size, 0, -1):
            rotate(r - s, c - s, r + s, c + s)

    for row in arr:
        answer = min(answer, sum(row))


print(answer)

'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''
