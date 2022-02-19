str1 = input()
str2 = input()

N = len(str1)
M = len(str2)

str1 = " " + str1
str2 = " " + str2

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])
'''
ACAYKP
CAPCAK
'''
