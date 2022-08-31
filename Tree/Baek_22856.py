import sys
sys.setrecursionlimit(10**6)


def init():
    N = int(input())
    visit = [None] + [False] * N
    tree = {vertex: [-1, -1] for vertex in range(1, N + 1)}
    parent = [-1] * (N + 1)
    for _ in range(N):
        a, b, c = tuple(map(int, input().split()))
        tree[a] = [b, c]

        if b != -1:
            parent[b] = a
        if c != -1:
            parent[c] = a

    return N, tree, parent, visit


def inorder(curr):
    if curr == -1:
        return
    inorder(tree[curr][0])
    inorder_result.append(curr)
    inorder(tree[curr][1])


def similar_inorder(curr):
    global count
    visit[curr] = True
    parent, left, right = parents[curr], tree[curr][0], tree[curr][1]

    if left != -1 and not visit[left]:
        similar_inorder(left)
        count += 1
    elif right != -1 and not visit[right]:
        similar_inorder(right)
        count += 1
    elif curr == inorder_result[-1]:
        return
    elif parent != -1:
        similar_inorder(parent)
        count += 1


N, tree, parents, visit = init()
count, root = 0, 1
inorder_result = list()
inorder(root)
similar_inorder(root)
print(count)

'''
7
1 2 3
2 4 5
3 6 7
4 -1 -1
5 -1 -1
6 -1 -1
7 -1 -1
'''
