N, K = tuple(map(int, input().split()))
weights = [int(input()) for _ in range(N)]
MAX_VALUE = 1000000 * 100


dp = [0] + [-1] * 100000

for weight in weights:
    dp[weight] = 1

for i in range(1, K + 1):
    min_value = MAX_VALUE
    for weight in weights:
        if dp[i - weight] != -1 and i - weight >= 0:
            min_value = min(min_value, dp[i - weight])
    if min_value != MAX_VALUE:
        dp[i] = min_value + 1

print(dp[K])

'''
3 15
1
5
12
'''
