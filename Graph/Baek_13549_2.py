from collections import deque

MAX = 100000
N, K = tuple(map(int, input().split()))
queue = deque()
visited = [False] * (MAX + 1)


def in_range(pos):
    return 0 <= pos <= MAX


def can_go(pos):
    return in_range(pos) and not visited[pos]


queue.append((N, 0))
visited[N] = True

while queue:
    current_pos, current_time = queue.popleft()

    left = current_pos - 1
    right = current_pos + 1
    jump = current_pos * 2

    if current_pos == K:
        print(current_time)
        break

    if can_go(jump):
        queue.appendleft((jump, current_time))
        visited[jump] = True
    if can_go(left):
        queue.append((left, current_time + 1))
        visited[left] = True
    if can_go(right):
        queue.append((right, current_time + 1))
        visited[right] = True

'''
5 17
'''
