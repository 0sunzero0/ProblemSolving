import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
tree = {vertex : [] for vertex in range(1, N + 1)}
dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


def make_tree():
    for _ in range(N - 1):
        start, end = tuple(map(int, input().split()))
        tree[start].append(end)
        tree[end].append(start)


def go(current_node):
    visited[current_node] = True
    dp[current_node][0] = 1

    for child_node in tree[current_node]:
        if not visited[child_node]:
            go(child_node)
            dp[current_node][1] += dp[child_node][0]
            dp[current_node][0] += min(dp[child_node][1], dp[child_node][0])


make_tree()
go(1)
print(min(dp[1][0], dp[1][1]))

'''
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
'''
'''
9
1 2
1 3
2 4
3 5
3 6
4 7
4 8
4 9
'''
