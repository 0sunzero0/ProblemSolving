N = int(input())
K = int(input())


# A[i][j] = i * j 배열에서 mid 값보다 같거나 작은 숫자의 개수를 구하는 함수
def count_lower(mid, N):
    count = 0
    for row in range(1, N + 1):
        count += min(mid//row, N)
    return count


left, right = 1, K
answer = 0

while left <= right:
    mid = (left + right) // 2

    # mid 보다 같거나 작은 수가 K개 이상이면
    if count_lower(mid, N) >= K:
        answer = mid
        right = mid - 1
    # mid 보다 같거나 작수가 K개 미만이면
    else:
        left = mid + 1

print(answer)

'''
3
7
'''
