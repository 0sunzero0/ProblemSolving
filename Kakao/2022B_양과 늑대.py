max_sheep = 0

def solution(info, edges):
    tree = {vertex: [] for vertex in range(len(info))}
    for edge in edges:
        start, end = edge[0], edge[1]
        tree[start].append(end)

    def dfs(vertex, sheep, wolf, next_vertexs):
        global max_sheep
        sheep += info[vertex] ^ 1
        wolf += info[vertex]

        if sheep <= wolf:
            return

        max_sheep = max(max_sheep, sheep)
        for next_vertex in tree[vertex]:
            next_vertexs.add(next_vertex)

        for next_vertex in next_vertexs:
            dfs(next_vertex, sheep, wolf, next_vertexs - set([next_vertex]))

    dfs(0, 0, 0, set())

    return max_sheep
