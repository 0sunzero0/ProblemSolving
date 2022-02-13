import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001
visited[N] = True
hq = [([0, N])]

while hq:
    time, pos = heapq.heappop(hq)
    if pos == K:
        print(time)
        break

    next_pos = pos * 2
    if next_pos < len(visited) and not visited[next_pos]:
        visited[next_pos] = True
        heapq.heappush(hq, (time, next_pos))

    for next_pos in (pos + 1, pos - 1):
        if next_pos >= 0 and next_pos < len(visited) and not visited[next_pos]:
            visited[next_pos] = True
            heapq.heappush(hq, (time + 1, next_pos))