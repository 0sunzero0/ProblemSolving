'''
- 배열 A의 순서를 바꾸면서, 위의 식에 넣기
    - 배열 순서 → N! -> permutations(arr)
- 위의 식의 결과를 힙이라는 자료구조에 넣기 (힙은 최대값과 최소값을 빠르게 찾는다.)
- 최댓값 출력하기
'''


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