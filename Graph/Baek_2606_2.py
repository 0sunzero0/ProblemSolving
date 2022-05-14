vertex_num = int(input())
edge_num = int(input())

parent = [vertex for vertex in range(vertex_num + 1)]


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


for _ in range(edge_num):
    start, end = map(int, input().split())
    union(parent, start, end)

count = 0
for vertex in range(1, vertex_num + 1):
    if find_parent(parent, vertex) == 1:
        count += 1

print(count - 1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
