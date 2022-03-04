def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for height in range(len(triangle)):
        line_width = len(triangle[height])
        for width in range(line_width):
            if width == 0:
                dp[height][width] = dp[height - 1][width] + triangle[height][width]

            elif width == line_width - 1:
                dp[height][width] = dp[height - 1][width - 1] + triangle[height][width]

            else:
                dp[height][width] = max(dp[height - 1][width], dp[height - 1][width - 1]) + triangle[height][width]
    return max(dp[-1])