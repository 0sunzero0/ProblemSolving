import sys

graph = [[]]
INT_MAX = sys.maxsize


def solution(n, s, a, b, fares):
    graph = [[INT_MAX] * (n + 1) for _ in range(n + 1)]
    cost = INT_MAX

    for fare in fares:
        start, end, weight = fare
        graph[start][end] = weight
        graph[end][start] = weight

    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for k in range(1, n + 1):
        cost = min(cost, graph[s][k] + graph[k][a] + graph[k][b])
    return cost
