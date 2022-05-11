N, M = map(int,input().split())
miro = [ [0] * (M + 1) ] + [ [0] + list(map(int,input().split())) for _ in range(N)]
dp = [ [0] * (M + 1) for _ in range(N + 1) ]

dp[1][1] = miro[1][1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j + 1 <= M and dp[i][j + 1] < dp[i][j] + miro[i][j + 1]:
            dp[i][j+1] = dp[i][j] + miro[i][j + 1]
        if i + 1 <= N and dp[i+1][j] < dp[i][j] + miro[i + 1][j]:
            dp[i + 1][j] = dp[i][j] + miro[i + 1][j]
        if i + 1 <= N and j + 1 <= M and dp[i + 1][j + 1] < dp[i][j] + miro[i + 1][j + 1]:
            dp[i + 1][j + 1] = dp[i][j] + miro[i + 1][j + 1]

print(dp[N][M])
