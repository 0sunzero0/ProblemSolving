import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
parent = [num for num in range(N + 1)]


def find_parent(element):
    if parent[element] != element:
        parent[element] = find_parent(parent[element])
    return parent[element]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    # 값이 더 짝은 쪽을 부모로
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    operation, a, b = tuple(map(int, input().split()))
    if operation == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''
