N = int(input())
M = int(input())
MAX_INT = 100000 * 100

# 초기값을 전부 아주 큰 값으로 설정
dist = [[MAX_INT] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 값 0으로 초기화
for i in range(1, N + 1):
    dist[i][i] = 0

# 그래프를 인접 행렬로 표현
for _ in range(M):
    a, b, cost = tuple(map(int, input().split()))
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있기에 최소로 초기화
    dist[a][b] = min(dist[a][b], cost)

# 거쳐갈 정점 1번부터 N번까지 정의
for k in range(1, N + 1):
    # 고정된 k에 대해 모든 쌍 (i, j) 확인
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 모든 쌍의 최단 거리(최소 비용) 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 최대값이 갱신되지 않았으므로, 갈 수 없는 경우
        if dist[i][j] == MAX_INT:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''
