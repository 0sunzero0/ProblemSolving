from collections import deque

N, M = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}
visited = [False] * (N+1)
count = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if visited[next_vertex] == False:
                visited[next_vertex] = True
                queue.append(next_vertex)

def dfs(v):
    visited[v] = True
    for next_vertex in graph[v]:
        if visited[next_vertex] == False:
            visited[next_vertex] = True
            dfs(next_vertex)

for v in range(1, N+1):
    if visited[v] == False:
        # bfs(v)
        dfs(v)
        count += 1

print(count)

'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
