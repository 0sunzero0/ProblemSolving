N, M = tuple(map(int, input().split()))
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0] * (sum(costs) + 1) for _ in range(N + 1)]
answer = 10 ** 7

for item in range(1, N + 1):
    memory, cost = memories[item], costs[item]
    dp[item][cost] = memory

for i in range(1, N + 1):
    memory, cost = memories[i], costs[i]
    for c in range(1, sum(costs) + 1):
        dp[i][c] = dp[i - 1][c]
        if c >= cost:
            dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - cost] + memory)

for i in range(1, N + 1):
    for c in range(1, sum(costs) + 1):
        if dp[i][c] >= M:
            answer = min(c, answer)

print(answer)

'''
5 60
30 10 20 35 40
3 0 3 5 4
'''
