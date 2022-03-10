from collections import deque

vertex_num = int(input())
edge_num = int(input())
graph = {v : [] for v in range(1, vertex_num + 1)}
visited = [0] * (vertex_num + 1)
count = 0

for _ in range(edge_num):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(v):
    global count
    visited[v] = 1

    for next_v in graph[v]:
        if visited[next_v] == 0:
            count += 1
            dfs(next_v)

def bfs(v):
    global count
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if visited[next_vertex] == 0:
                visited[next_vertex] = 1
                count += 1
                queue.append(next_vertex)

# bfs(1)
dfs(1)

print(count)
