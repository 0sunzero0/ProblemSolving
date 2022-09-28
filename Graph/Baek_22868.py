from collections import deque, defaultdict


def make_graph():
    graph = defaultdict(list)
    for _ in range(M):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    for vertex in range(1, N + 1):
        graph[vertex].sort()
    return graph


def push(vertex, path, new_step):
    bfs_queue.append((vertex, path))
    visit[vertex] = True
    step[vertex] = new_step


def go_to_end():
    push(S, list(), 0)

    while bfs_queue:
        vertex, path = bfs_queue.popleft()
        for next_vertex in graph[vertex]:
            if not visit[next_vertex]:
                push(next_vertex, path + [next_vertex], step[vertex] + 1)
        if vertex == E:
            return path, step[E]


def initialize(path):
    for vertex in range(N + 1):
        visit[vertex] = False
        step[vertex] = 0

    for vertex in path:
        visit[vertex] = True


def go_to_start():
    push(E, list(), 0)

    while bfs_queue:
        vertex, path = bfs_queue.popleft()
        for next_vertex in graph[vertex]:
            if not visit[next_vertex]:
                push(next_vertex, path + [next_vertex], step[vertex] + 1)

    return step[S]


N, M = tuple(map(int, input().split()))
graph = make_graph()
S, E = tuple(map(int, input().split()))

bfs_queue = deque()
visit = [False] * (N + 1)
step = [0] * (N + 1)

first_path, first_path_len = go_to_end()
initialize(first_path)
bfs_queue = deque()
second_path_len = go_to_start()

print(first_path_len + second_path_len)

'''
4 5
1 2
1 3
2 3
2 4
3 4
1 4
'''
