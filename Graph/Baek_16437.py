import sys
input = sys.stdin.readline

N = int(input())
sys.setrecursionlimit(3 * N)

tree_up = [[] for _ in range(N + 1)]
vertex_to_info = [[], [0, 0]]

for vertex in range(2, N + 1):
    ti, ai, pi = tuple(input().split())
    ai, pi = int(ai), int(pi)
    tree_up[pi].append(vertex)
    vertex_to_info.append([ti, ai])


def go(current_vertex):
    answer = 0
    for next_vertex in tree_up[current_vertex]:
        answer += go(next_vertex)

    if current_vertex != 1 and vertex_to_info[current_vertex][0] == 'S':
        answer += vertex_to_info[current_vertex][1]
    elif current_vertex != 1 and vertex_to_info[current_vertex][0] == 'W':
        answer -= vertex_to_info[current_vertex][1]

    if answer <= 0:
        answer = 0
    return answer


print(go(1))

'''
4
S 100 3
W 50 1
S 10 1
'''
