import sys

weight_num, goal_value = map(int, sys.stdin.readline().split())
weights = []
dp = [0 for _ in range(goal_value+1)]
dp[0] = 1

for _ in range(weight_num):
    weights.append(int(sys.stdin.readline().strip()))

# 중복 제거
weights = list(set(weights))

for weight in weights:
    for value in range(1, goal_value+1):
        if value - weight >= 0:
            dp[value] += dp[value-weight]

print(dp[goal_value])
