def go(arr, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    if index == len(arr):
        return
    go(arr, index + 1, lotto + [arr[index]])
    go(arr, index + 1, lotto)

while True:
    length, *arr = list(map(int,input().split()))
    if length == 0:
        break

    go(arr, 0, [])
    print()

'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''
