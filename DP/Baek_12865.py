N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
things = [[0, 0]]
for _ in range(N):
    things.append(list(map(int, input().split())))

for i in range(1, N+1):
    for w in range(1, K+1):
        weight = things[i][0]
        value = things[i][1]
        dp[i][w] = dp[i - 1][w]
        if w - weight >= 0:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)

print(dp[N][K])

'''
4 7
6 13
4 8
3 6
5 12
'''
