import sys
sys.setrecursionlimit(10000)

def make_tree():
    for vertex in range(1, N + 1):
        tree[vertex] = []

    for _ in range(N - 1):
        A, B = tuple(map(int, input().split()))
        tree[B].append(A)


def find_parent(vertex):
    if vertex == root_node:
        return
    parent.append(tree[vertex][0])
    find_parent(tree[vertex][0])


def find_near_common_parent(A, B):
    global parent
    find_parent(A)
    A_parent = parent
    parent = []
    find_parent(B)
    B_parent = parent
    find_common_parent = [element for element in [A] + A_parent  if element in [B] + B_parent]

    return find_common_parent[0]


for _ in range(int(input())):
    N = int(input())
    tree = {}
    parent = []

    make_tree()
    for key, value in tree.items():
        if len(value) == 0:
            root_node = key
            break
    vertex_A, vertex_B = tuple(map(int, input().split()))
    print(find_near_common_parent(vertex_A, vertex_B))
