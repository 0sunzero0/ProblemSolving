from collections import defaultdict
import sys

MAX_INT = 1000000000 + 1
N, Q = tuple(map(int, input().split()))
tree = defaultdict(list)
sys.setrecursionlimit(2 * N)


def make_tree():
    for _ in range(N - 1):
        start, end, weight = tuple(map(int, input().split()))
        tree[start].append((end, weight))
        tree[end].append((start, weight))


def count_fitted_USADO(vertex, cost):
    global answer
    for next_vertex, weight in tree[vertex]:
        if not visited[next_vertex]:
            next_cost = cost

            if cost > weight:
                next_cost = weight

            if k <= next_cost:
                answer += 1

            visited[next_vertex] = True
            count_fitted_USADO(next_vertex, next_cost)


make_tree()
for _ in range(Q):
    k, v = tuple(map(int, input().split()))
    visited = [False] * (N + 1)
    answer = 0

    visited[v] = True
    count_fitted_USADO(v, MAX_INT)

    print(answer)

'''
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1
'''
