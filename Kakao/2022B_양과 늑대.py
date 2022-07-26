answer = 0

def solution(info, edges):
    global answer
    N = len(info)

    # tree 만들기
    tree = {vertex: [] for vertex in range(N)}
    for edge in edges:
        start, end = edge
        tree[start].append(end)

    # 백트레킹 함수
    def go(current_vertex, sheep, wolf, next_vertexs):
        global answer

        sheep += info[current_vertex] ^ 1  # xor
        wolf += info[current_vertex]

        if sheep <= wolf:
            return

        answer = max(answer, sheep)

        for next_vertex in tree[current_vertex]:
            next_vertexs.add(next_vertex)

        for next_vertex in next_vertexs:
            go(next_vertex, sheep, wolf, next_vertexs - set([next_vertex]))

    # 백트레킹 함수 호출
    go(0, 0, 0, set())

    return answer
