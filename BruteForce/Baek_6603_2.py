from itertools import combinations

while True:
    length, *arr = list(map(int,input().split()))
    if length == 0:
        break

    cases = list(combinations(arr, 6))

    for case in cases:
        print(*case)
    print()

'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
