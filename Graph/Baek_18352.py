from collections import deque
import sys

def bfs(start):
    global visited
    queue = deque([start])
    visited[start] = 0

    while queue:
        vertex = queue.popleft()
        for linked_vertex in graph[vertex]:
            if visited[linked_vertex] == -1:
                queue.append(linked_vertex)
                visited[linked_vertex] = visited[vertex] + 1

# init
input = sys.stdin.readline
vertex_num, edge_num, shortest_path, start = map(int, input().split())
graph = {vertex : [] for vertex in range(1, vertex_num+1)}
answer = []
for _ in range(edge_num):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1] * (vertex_num + 1)

# 시작점 넣고, 탐색
bfs(start)

# 목표거리가 K인 경우, list에 추가
for vertex in range(len(visited)):
    if visited[vertex] == shortest_path:
        answer.append(vertex)

if len(answer) == 0:
    print(-1)
else:
    for vertex in answer:
        print(vertex)
