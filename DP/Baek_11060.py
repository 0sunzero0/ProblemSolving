N = int(input())
arr = list(map(int, input().split()))
dp = [-1] * N
dp[0] = 0

for current in range(0, N-1):
    if dp[current] == -1:
        continue

    for next_step in range(1, arr[current] + 1):
        if current + next_step >= N:
            break
        if dp[current + next_step] == -1 or dp[current + next_step] > dp[current] + 1:
            dp[current + next_step] = dp[current] + 1

print(dp[N-1])

'''
10
1 2 0 1 3 2 1 5 4 2
'''
