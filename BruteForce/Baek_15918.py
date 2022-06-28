N, X, Y = tuple(map(int, input().split()))
arr = [0] * (2 * N + 1)
arr[X] = arr[Y] = Y - X - 1
answer = 0


def go(depth):
    global answer
    if depth == Y - X - 1:
        go(depth + 1)

    if depth == N + 1:
        answer += 1
        return

    for i in range(1, 2 * N - depth):
        if arr[i] == 0 and arr[i + depth + 1] == 0:
            arr[i] = arr[i + depth + 1] = depth
            go(depth + 1)
            arr[i] = arr[i + depth + 1] = 0


go(1)
print(answer)

'''
3 1 5
'''
