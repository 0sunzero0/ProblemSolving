N, M = tuple(map(int, input().split()))
MAX_INT = N * (N * (N - 1) / 2) + 1
graph = [[MAX_INT] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = tuple(map(int, input().split()))
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        # 자기 자신이 아니면서, 최단 거리가 갱신되어 있다면, 연결
        if 0 < graph[i][j] < MAX_INT or 0 < graph[j][i] < MAX_INT:
            count += 1

    if count == N - 1:
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
