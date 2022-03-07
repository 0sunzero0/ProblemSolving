from collections import deque

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph:
    graph[key].sort()

def init():
    global visited
    visited = [False] * (N + 1)
    print()

def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=' ')
    for next_vertex in graph[vertex]:
        if visited[next_vertex] == False:
            dfs(next_vertex)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for next_vertex in graph[vertex]:
            if visited[next_vertex] == False:
                queue.append(next_vertex)
                visited[next_vertex] = True

dfs(V)
init()
bfs(V)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
