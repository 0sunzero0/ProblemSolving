import sys
input = sys.stdin.readline

N, d, k, c = tuple(map(int, input().split()))

sushi = [int(input()) for _ in range(N)]
sushi.extend(sushi)

result = 0

for i in range(2 * N - k):
    result = max(result, len(set(sushi[i:i + k] + [c])))

print(result)

'''
8 30 4 30
7
9
7
30
2
7
9
25
'''
