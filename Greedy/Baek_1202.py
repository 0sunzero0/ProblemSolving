import sys
import heapq
input = sys.stdin.readline

N, K = tuple(map(int, input().split()))

jewel_infos = list()
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewel_infos, [weight, value])

bag_infos = list()
for _ in range(K):
    heapq.heappush(bag_infos, int(input()))

answer = 0
capable_jewel = []

for _ in range(K):
    bag_weight = heapq.heappop(bag_infos)
    while jewel_infos and bag_weight >= jewel_infos[0][0]:
        [weight, value] = heapq.heappop(jewel_infos)
        heapq.heappush(capable_jewel, - value)

    if capable_jewel:
        answer = answer - heapq.heappop(capable_jewel)

print(answer)

'''
3 2
1 65
5 23
2 99
10
2
'''
