N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
dp = [1] * (N+1)

max_value = 1

for i in range(1, N+1):
    for j in range(1, i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + 1, dp[i])

for i in range(1, N+1):
    max_value = max(max_value, dp[i])
print(max_value)

'''
6
10 20 10 30 20 50
'''
'''
6
30 20 10 20 30 40
'''
