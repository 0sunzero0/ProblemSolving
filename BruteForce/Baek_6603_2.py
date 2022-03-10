from itertools import combinations

input_array = []
while True:
    input_array = list(map(int, input().split()))
    input_array.pop(0)
    if len(input_array) == 0:
        break

    cases = list(combinations(input_array, 6))

    for case in cases:
        print(*case)
    print()
