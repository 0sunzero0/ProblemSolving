N, M = map(int, input().split())
visited = [False] * N
selected = []


def go(depth):
    if depth == M:
        print(*selected)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            selected.append(i+1)

            go(depth+1)

            visited[i] = False
            selected.pop()


go(0)
'''
3 1
'''
'''
4 2
'''
