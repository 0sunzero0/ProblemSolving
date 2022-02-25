from collections import deque
INF = 1e9

# 입력 받기
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

shark_size = 2
cur_x, cur_y = 0, 0

total_distance = 0
eat = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 최단거리 찾는 함수 bfs
def bfs():
    # distance -1로 초기화
    distance = [[-1] * N for _ in range(N)]
    # 시작위치 queue에 넣기
    queue = deque([(cur_x, cur_y)])
    distance[cur_x][cur_y] = 0
    # queue가 빌 때까지, 탐색
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        # 다음 위치가 0이상 n보다 작으면
            if 0 <= nx < N and 0 <= ny < N:
                # 또한, 아직 방문하지 않고, 물고기의 크기가 지금 상어의 크기보다 작거나 같으면
                if distance[nx][ny] == -1 and graph[x][y] <= shark_size:
                    # distance += 1
                    distance[nx][ny] = distance[x][y] + 1
                    # queue에 다음위치 넣기
                    queue.append((nx, ny))
    return distance

# 먹을 수 있는 물고기의 위치 찾는 함수 find
def find():
    # BFS 탐색해 최단거리를 찾는다. (최단거리 배열 채우기)
    shortest_distance = INF
    distance = bfs()
    # 도달이 가능하면서 먹을 수 있는 물고기일 때, 가장 가까운 물고기 한 마리만 선택
    # 최단거리 배열을 순회한다.
    for i in range(N):
        for j in range(N):
            # distance -1이 아니고, 해당 물고기의 크기가 1이상이고, 해당 물고기가 상어의 크기보다 작으면,
            if distance[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                # 순회하면서, 그 중 거리가 가장 가까운 물고기 갱신
                if distance[i][j] < shortest_distance:
                    shortest_distance = distance[i][j]
                    x, y = i, j

    if shortest_distance == INF:
        return None
    else :
        return x, y, shortest_distance

# 1. 9의 위치를 찾아 start pos로 두자. 그 위치엔 아무것도 없다고 처리한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            cur_x, cur_y = i, j
            graph[cur_x][cur_y] = 0

# 2. 먹을 수 있는 물고기의 위치 찾기
while True:
    value = find()
    # 3. 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력한다.
    if value == None:
        print(total_distance)
        break
    # 4. 먹을 수 있는 물고기가 있는 경우, 위치를 받아, 해당 위치로 이동하고 먹는다. 해당 위치는 0으로 표시한다.
    else:
        cur_x, cur_y = value[0], value[1]
        total_distance += value[2]
        eat += 1
        graph[cur_x][cur_y] = 0
        # 5. 아기 상어의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가시킨다.
        if eat >= shark_size:
            shark_size += 1
            eat = 0

'''
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
'''
