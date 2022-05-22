import heapq
import sys
input = sys.stdin.readline

vertex_num, edge_num = map(int, input().split())
start = int(input())
graph = [[] for _ in range(vertex_num + 1)]

for _ in range(edge_num):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))

distance = [20001 * 10] * (vertex_num + 1)
distance[start] = 0

# 최소 힙 생성
Q = []
heapq.heappush(Q, (0, start))

# 거리 정보들이 모두 소진될 때까지 거리 갱신을 반복한다.
while Q:
    distance_x, x = heapq.heappop(Q)

    # 꺼낸 정보가 최신 정보랑 다르면, 의미없는 정보이므로 pass
    if distance[x] != distance_x: continue

    # 연결된 모든 간선들을 통해서 다른 정점들에 대한 정보를 갱신해준다.
    for u, weight in graph[x]:
        # u 까지 갈 수 있는 더 짧은 거리를 찾았다면 이에 대한 정보를 갱신하고 PQ에 기록해준다.
        if distance[u] > distance[x] + weight:
            distance[u] = distance[x] + weight
            heapq.heappush(Q, (distance[u], u))

for i in range(1, vertex_num + 1):
    # 도달할 수 있는 경우 거리 출력
    if distance[i] != 20001 * 10:
        print(distance[i])
    # 도달할 수 없는 경우
    else:
        print('INF')
