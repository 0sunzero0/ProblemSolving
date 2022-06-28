N, B, W = tuple(map(int, input().split()))
path = list(input().strip())

left, right, answer = 0, 0, 0
white, black = 0, 0


def process_left(idx):
    global white, black
    if path[idx] == 'W':
        white -= 1
    elif path[idx] == 'B':
        black -= 1


def process_right(idx):
    global white, black
    if path[idx] == 'W':
        white += 1
    elif path[idx] == 'B':
        black += 1


while left <= right < N:
    if black > B:
        process_left(left)
        left += 1

    else:
        process_right(right)
        right += 1

    if black <= B and white >= W:
        answer = max(answer, right - left)

print(answer)

'''
10 1 2
WBBWWBWWBW
'''
