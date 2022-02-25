N = int(input())-1
arr = list(map(int,input().split()))
goal = arr[-1]
arr = arr[:-1]

dp = [[0]*21 for _ in range(N)]
dp[0][arr[0]] = 1

for i in range(1, N):
    for j in range(21):
        if 0 <= j-arr[i] <= 20:
            dp[i][j] += dp[i-1][j-arr[i]]
        if 0 <= j+arr[i] <= 20:
            dp[i][j] += dp[i-1][j+arr[i]]

print(dp[N-1][goal])
