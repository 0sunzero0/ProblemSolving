N, M = tuple(map(int, input().split()))
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = tuple(map(int, input().split()))
    graph[a][b] = 1
    graph[b][a] = -1

count = [0] * (N + 1)
answer = 0


def go_parent(current_vertex, start):
    for next_vertex in range(1, N + 1):
        if graph[current_vertex][next_vertex] == 1 and not visited[next_vertex]:
            visited[next_vertex] = True
            count[start] += 1
            go_parent(next_vertex, start)


def go_child(current_vertex, start):
    for next_vertex in range(1, N + 1):
        if graph[current_vertex][next_vertex] == -1 and not visited[next_vertex]:
            visited[next_vertex] = True
            count[start] += 1
            go_child(next_vertex, start)


for vertex in range(1, N + 1):
    visited = [False] * (N + 1)

    # 부모 노드 찾기
    visited[vertex] = True
    go_parent(vertex, vertex)

    visited = [False] * (N + 1)

    # 자식 노드 찾기
    visited[vertex] = True
    go_child(vertex, vertex)

    # 자신을 제외한 노드의 개수가 N-1이라면 정답
    if count[vertex] == N - 1:
        answer += 1

print(answer)

'''
6 6
1 5
3 4
5 4
4 2
4 6
5 2
'''
