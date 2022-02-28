from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for num in range(1, N+1):
    for case in list(combinations(arr, num)):
        if sum(case) == S:
            count += 1

print(count)
