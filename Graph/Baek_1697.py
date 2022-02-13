import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001

queue = deque()
queue.append(N)
visited[N] = 0


while queue:
    pos = queue.popleft()
    if pos == K:
        print(visited[pos])
        break

    for next_pos in (pos -1, pos + 1, pos * 2):
        if 0 <= next_pos < len(visited) and visited[next_pos] == -1:
            queue.append(next_pos)
            visited[next_pos] = visited[pos] + 1
