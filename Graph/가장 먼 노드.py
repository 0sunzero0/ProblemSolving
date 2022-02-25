'''
1. vertex로 그래프 표현하기
    dictionary로 표현하여, 인접리스트를 구현하면 시간을 줄이자.
2. BFS 탐색 (visited 배열 방문하면서 체크)
    1. queue start vertex인 1 넣기
    2. queue가 비어 있을 때까지, 반복
        - queue에 현재 값 넣기, 방문 현재값 처리
        - (반복문을 통해) queue와 연결된 값들을 방문
        0 해당 값이 방문 안되었다면, queue에 넣고 해당 visited 배열에도 현재 값의 visited 배열 +1의 값 넣기
3. visited 배열로 다 방문했다면 (= 큐가 비었다면), 가장 큰 수를 찾고 그 수의 갯수를 구하기
'''


from collections import deque


def init(n, edge):
    graph = {i: [] for i in range(1, n + 1)}

    for one_edge in edge:
        i = one_edge[0]
        j = one_edge[1]
        graph[i].append(j)
        graph[j].append(i)

    for key in graph:
        graph[key].sort()

    visited = [0] * (n + 1)
    return graph, visited


def solution(n, edge):
    graph, visited = init(n, edge)
    queue = deque([1])
    visited[1] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[v] + 1

    max_num = max(visited)
    answer = visited.count(max_num)
    return answer
