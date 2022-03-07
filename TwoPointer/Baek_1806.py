N, S = map(int, input().split())
num = list(map(int, input().split()))
cumulated_sum = [num[0]] * N

for i in range(1, N):
    cumulated_sum[i] = cumulated_sum[i-1] + num[i]

left, right = 0, 0
min_value = N + 1

while True:
    if left > right or right == N:
        break

    if left == 0:
        prefix_sum = cumulated_sum[right]
    else:
        prefix_sum = cumulated_sum[right] - cumulated_sum[left-1]

    section = right - left + 1
    if prefix_sum < S:
        right += 1
    elif prefix_sum > S:
        min_value = min(section, min_value)
        left += 1
        if left > right and left < N:
            right = left
    else:
        min_value = min(section, min_value)
        right += 1

if min_value > N:
    print(0)
else:
    print(min_value)
