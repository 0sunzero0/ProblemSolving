N = int(input())
stairs_score = [0] * (N + 1)
for i in range(1, N + 1):
    stairs_score[i] = int(input())

dp = [[0] * 3 for _ in range(N + 1)]
dp[1][1] = stairs_score[1]
if N >= 2:
    dp[2][1] = stairs_score[2]
    dp[2][2] = stairs_score[1] + stairs_score[2]

for i in range(3, N + 1):
    for j in range(1, 3):
        if j == 2:
            dp[i][j] = dp[i - 1][1] + stairs_score[i]
        elif j == 1:
            dp[i][j] = max(dp[i - 2][1], dp[i - 2][2]) + stairs_score[i]

print(max(dp[N][1], dp[N][2]))

'''
6
10
20
15
25
10
20
'''
