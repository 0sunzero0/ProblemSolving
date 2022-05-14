N, M = map(int, input().split())
parent = [vertex for vertex in range(N + 1)]


def find_parent(parent, v):
    if parent[v] != v:
        parent[v] = find_parent(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    start, end = map(int, input().split())
    union(parent, start, end)

answer = []
for a in parent:
    answer.append(find_parent(parent, a))

answer = answer[1:]
print(len(set(answer)))
