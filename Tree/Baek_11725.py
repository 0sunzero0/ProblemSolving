import sys

N = int(input())
graph = {vertex : [] for vertex in range(1, N + 1)}
parents = [0] * (N + 1)
sys.setrecursionlimit(100000)

for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(vertex, parent):
        for next_vertex in graph[vertex]:
            if next_vertex == parent:
                continue
            parents[next_vertex] = vertex
            dfs(next_vertex, vertex)

dfs(1, -1)

for vertex in range(2, N + 1):
    print(parents[vertex])

'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
