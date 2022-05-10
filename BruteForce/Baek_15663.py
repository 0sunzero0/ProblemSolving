N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [False] * N
selected = []


def go(depth):
    if depth == M:
        print(*selected)
        return

    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != arr[i]:
            visited[i] = True
            selected.append(arr[i])
            go(depth + 1)

            visited[i] = False
            selected.pop()
            overlap = arr[i]


go(0)
'''
3 1
4 4 2
'''
'''
4 2
9 7 9 1
'''
'''
4 4
1 1 1 1
'''
