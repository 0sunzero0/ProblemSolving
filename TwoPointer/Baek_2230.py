N, M = tuple(map(int, input().split()))
A = list()
for _ in range(N):
    A.append(int(input()))
A.sort()

left = 0
right = 0

answer = 2 * (10 ** 9)

while left <= right < N:
    diff = abs(A[right] - A[left])
    if diff > M:
        answer = min(answer, diff)
        left += 1
    elif diff == M:
        answer = diff
        break
    elif diff < M:
        right += 1

print(answer)

'''
3 3
1
5
3
'''
