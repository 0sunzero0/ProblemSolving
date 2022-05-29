import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, R, Q = tuple(map(int, input().split()))
size = [0] * (N + 1)
tree = {vertex : [] for vertex in range(1, N + 1)}
visited = [False] * (N + 1)


def make_tree():
    for _ in range(N - 1):
        start, end = tuple(map(int, input().split()))
        tree[start].append(end)
        tree[end].append(start)


def count_subtree_nodes(current_node):
    size[current_node] = 1
    visited[current_node] = True

    for node in tree[current_node]:
        if not visited[node]:
            count_subtree_nodes(node)
            size[current_node] += size[node]


make_tree()
count_subtree_nodes(R)

for _ in range(Q):
    query = int(input())
    print(size[query])

'''
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8
'''
