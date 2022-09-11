from collections import defaultdict

while True:
    N, K = tuple(map(int, input().split()))
    if (N, K) == (0, 0):
        break

    arr = list(map(int, input().split()))
    parents = defaultdict(int)

    p_idx = 0
    for c_idx in range(1, N):
        parents[arr[c_idx]] = arr[p_idx]
        if c_idx < N - 1 and arr[c_idx] + 1 < arr[c_idx + 1]:
            p_idx += 1

    count = 0
    if parents[parents[K]]:
        for node in arr:
            if parents[parents[K]] == parents[parents[node]] and parents[K] != parents[node]:
                count += 1

    print(count)

'''
10 15
1 3 4 5 8 9 15 30 31 32
12 9
3 5 6 8 9 10 13 15 16 22 23 25
10 4
1 3 4 5 8 9 15 30 31 32
0 0
'''
