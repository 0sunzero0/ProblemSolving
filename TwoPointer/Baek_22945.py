N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1
section = N - 2
max_ability = 0

while left <= right:
    current_ability = (right - left - 1) * min(arr[left], arr[right])
    max_ability = max(max_ability, current_ability)
    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_ability)

'''
4
1 4 2 5
'''
