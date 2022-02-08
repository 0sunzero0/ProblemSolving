N, K = map(int, input().split())

thing = [[0, 0]]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(N):
    thing.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = thing[i][0]
        value = thing[i][1]

        # 무게가 허용무게 보다 크면,
        if weight > j:
            # 이 물건을 담지 않고 이전 물건까지 담았을 때 가방에 담을 수 있는 최고 가치를 저장한다.
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 물건을 넣지 않았을 때와 현재 물건을 넣었을 때의 가치를 비교한다.
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])
'''
4 7
6 13
4 8
3 6
5 12
'''