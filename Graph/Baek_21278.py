from collections import defaultdict

MAX_INT = 100 * 100 * 2
N, M = tuple(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(M)]
graph = defaultdict(list)

dist = [[MAX_INT] * (N + 1) for _ in range(N + 1)]
time = MAX_INT
building = [1, 2]


def make_graph():
    for edge in edges:
        start, end = edge
        graph[start].append(end)
        graph[end].append(start)
        dist[start][end] = 1
        dist[end][start] = 1


def preprocessing():
    for i in range(1, N + 1):
        dist[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def combination():
    global building, time
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            now = 0
            for k in range(1, N + 1):
                if i == k or j == k:
                    continue
                now += min(dist[i][k], dist[j][k])
            if time > now:
                building = [i, j]
                time = now


make_graph()
preprocessing()
combination()
print(building[0], building[1], time * 2)

'''
5 4
1 3
4 2
2 5
3 2
'''
