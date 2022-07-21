import heapq

T, N = tuple(map(int, input().split()))
priority_queue = list()

for _ in range(N):
    a, b, c = tuple(map(int, input().split()))
    heapq.heappush(priority_queue, (-c, a, b))


for _ in range(T):
    c, a, b = heapq.heappop(priority_queue)
    print(a)
    b -= 1
    c += 1
    if b != 0:
        heapq.heappush(priority_queue, (c, a, b))

'''
8 2
1 5 1
2 5 1
'''
'''
10 2
1 10 1000
2 10 1
'''
