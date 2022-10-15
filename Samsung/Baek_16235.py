def init():
    N, M, K = tuple(map(int, input().split()))
    food = [[5] * N for _ in range(N)]
    plus_food = [list(map(int, input().split())) for _ in range(N)]
    tree = [[list() for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        r, c, age = tuple(map(int, input().split()))
        tree[r - 1][c - 1].append(age)

    return N, M, K, food, plus_food, tree


def spring():
    global tree
    died_tree = []

    for r in range(N):
        for c in range(N):
            tree[r][c].sort()
            for t in range(len(tree[r][c])):
                age = tree[r][c][t]
                if food[r][c] >= age:
                    food[r][c] -= age
                    tree[r][c][t] += 1
                else:
                    died_tree.append((r, c, tree[r][c][t:]))
                    tree[r][c] = tree[r][c][:t]
                    break

    return died_tree


def summer(died_tree):
    for r, c, ages in died_tree:
        for age in ages:
            food[r][c] += age // 2


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def autumn():
    global tree
    # 왼 왼위 위 오위  오 오아래 아래 왼아래
    drs = [-1, 0, 1, -1, 1, -1, 0, 1]
    dcs = [-1, -1, -1, 0, 0, 1, 1, 1]

    for r in range(N):
        for c in range(N):
            for age in tree[r][c]:
                if age % 5 == 0:
                    for d in range(8):
                        nr, nc = r + drs[d], c + dcs[d]
                        if in_range(nr, nc):
                            tree[nr][nc].append(1)


def winter():
    for r in range(N):
        for c in range(N):
            food[r][c] += plus_food[r][c]


def get_live_tree_cnt():
    result = 0
    for r in range(N):
        for c in range(N):
            result += len(tree[r][c])
    return result


def simulate():
    died_tree = spring()
    summer(died_tree)
    autumn()
    winter()


N, M, K, food, plus_food, tree = init()
for _ in range(K):
    simulate()
print(get_live_tree_cnt())

'''
1 1 1
1
1 1 1
'''
'''
5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
'''
'''
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3
'''
