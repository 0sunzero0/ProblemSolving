from itertools import permutations

N, M = map(int, input().split())
array = [num for num in range(1, N + 1)]
cases = list(permutations(array, M))
for case in cases:
    print(*case)
