from itertools import combinations

N = int(input())
members = [num for num in range(1, N+1)]
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = 100*10

cases = list(combinations(members, N//2))
for idx in range(0, len(cases)//2):
    case = cases[idx]
    first = []
    second = []

    first_capability = 0
    second_capability = 0

    for member in members:
        if member in case:
            first.append(member)
        else:
            second.append(member)

    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                first_capability += S[first[i]-1][first[j]-1]
                second_capability += S[second[i]-1][second[j]-1]

    diff = abs(first_capability - second_capability)
    min_diff = min(min_diff, diff)

print(min_diff)

'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
