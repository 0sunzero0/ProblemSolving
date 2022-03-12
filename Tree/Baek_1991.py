N = int(input())
graph = {chr(vertex + 65) : ['.', '.'] for vertex in range(0, N+1)}

def init():
    for _ in range(N):
        vertex, left, right = input().strip().split()
        graph[vertex][0], graph[vertex][1] = left, right

def pre_order(vertex):
    if vertex == '.':
        return
    print(vertex, end='')
    pre_order(graph[vertex][0])
    pre_order(graph[vertex][1])

def in_order(vertex):
    if vertex == '.':
        return
    in_order(graph[vertex][0])
    print(vertex, end='')
    in_order(graph[vertex][1])

def post_order(vertex):
    if vertex == '.':
        return
    post_order(graph[vertex][0])
    post_order(graph[vertex][1])
    print(vertex, end='')

init()
pre_order('A')
print()
in_order('A')
print()
post_order('A')

'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
