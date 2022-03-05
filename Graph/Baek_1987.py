import sys

input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(map(lambda x : ord(x) - 65, input().rstrip())) for _ in range(R)]

visited = [False] * 26
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visited[graph[0][0]] = True
max_count = 1

def dfs(y, x, count):
    global max_count
    max_count = max(count, max_count)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < R and 0 <= nx < C and visited[graph[ny][nx]] == False:
                visited[graph[ny][nx]] = True
                dfs(ny, nx, count + 1)
                visited[graph[ny][nx]] = False

dfs(0, 0, 1)
print(max_count)

'''
2 4
CAAB
ADCB
'''
