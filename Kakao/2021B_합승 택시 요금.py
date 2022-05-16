import heapq
import sys

graph = [[]]
INT_MAX = sys.maxsize


def dijkstra(start, end):
    global graph
    n = len(graph)
    pq = []
    dist = [INT_MAX] * (n + 1)

    dist[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        min_dist, min_index = heapq.heappop(pq)

        if min_dist != dist[min_index]:
            continue

        for target_index, target_dist in graph[min_index]:
            new_dist = dist[min_index] + target_dist

            if new_dist < dist[target_index]:
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))

    return dist[end]


def solution(n, s, a, b, fares):
    global graph
    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        start, end, weight = fare
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    cost = dijkstra(s, a) + dijkstra(s, b)

    for k in range(1, n + 1):
        if s != k:
            cost = min(cost, dijkstra(s, k) + dijkstra(k, a) + dijkstra(k, b))

    return cost
