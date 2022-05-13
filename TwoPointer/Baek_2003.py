N, M = tuple(map(int, input().split()))
num = list(map(int, input().split()))

cumulated_sum = [num[0]] * N
count = 0

if N >= 2:
    for i in range(1, N):
        cumulated_sum[i] = cumulated_sum[i - 1] + num[i]

left, right = 0, 0
while left <= right < N:

    if left == 0:
        prefix_sum = cumulated_sum[right]
    else:
        prefix_sum = cumulated_sum[right] - cumulated_sum[left - 1]

    if prefix_sum < M:
        right += 1
    elif prefix_sum > M:
        left += 1
        if right < left < N:
            right = left
    else:
        count += 1
        right += 1

print(count)

'''
4 2
1 1 1 1
'''
'''
10 5
1 2 3 4 2 5 3 1 1 2
'''
