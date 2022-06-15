from collections import deque

MAX = 100000
N, K = tuple(map(int, input().split()))
visited = [-1] * (MAX + 1)
queue = deque()

visited[N] = 0
queue.append(N)


def in_range(pos):
    return 0 <= pos <= MAX


def can_go(pos):
    return in_range(pos) and visited[pos] == -1


while queue:
    current_pos = queue.popleft()

    if current_pos == K:
        print(visited[current_pos])
        break

    if can_go(current_pos * 2):
        queue.appendleft(current_pos * 2)
        visited[current_pos * 2] = visited[current_pos]
    if can_go(current_pos - 1):
        queue.append(current_pos - 1)
        visited[current_pos - 1] = visited[current_pos] + 1
    if can_go(current_pos + 1):
        queue.append(current_pos + 1)
        visited[current_pos + 1] = visited[current_pos] + 1

'''
5 17
'''
