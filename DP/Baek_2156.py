N = int(input())
grapes = [0]
for _ in range(N):
    grapes.append(int(input()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        dp[1] = grapes[1]
    elif i == 2:
        dp[2] = grapes[1] + grapes[2]
    else:
        dp[i] = max(dp[i - 3] + grapes[i - 1] + grapes[i], dp[i - 2] + grapes[i], dp[i - 1])

print(dp[N])

'''
6
6
10
13
9
8
1
'''
