N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

def dfs(vertex, parent):
        for next_vertex in graph[vertex]:
            if next_vertex == parent:
                continue
            parent[next_vertex] = vertex
            dfs(next_vertex, vertex)

dfs(1, -1)

for vertex in range(2, N + 1):
    print(parent[vertex])
