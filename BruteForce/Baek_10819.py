from itertools import permutations
import heapq

N = int(input())
A = list(map(int, input().split()))
heap = []

cases = list(permutations(A))
answer = 0

for case in cases:
    sum = 0
    for i in range(N - 1):
        sum += abs(case[i] - case[i + 1])
    heapq.heappush(heap, (-sum, sum))

print(heap[0][1])

'''
6
20 1 15 8 4 10
'''
