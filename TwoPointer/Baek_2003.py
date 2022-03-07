length, sum = map(int, input().split())
num = list(map(int, input().split()))
cumulated_sum = [num[0]] * (length)
count = 0

if length >= 2:
    for i in range(1, length):
        cumulated_sum[i] = cumulated_sum[i-1] + num[i]

left, right = 0, 0
while True:
    if left > right or right >= length :   break

    if left == 0:
        prefix_sum = cumulated_sum[right]
    else:
        prefix_sum = cumulated_sum[right] - cumulated_sum[left-1]

    if prefix_sum < sum:
        right += 1
    elif prefix_sum > sum:
        left += 1
        if left > right and left < length:
            right = left
    else:
        count += 1
        right += 1

print(count)

'''
4 2
1 1 1 1
'''
