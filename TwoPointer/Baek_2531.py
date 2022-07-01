from collections import defaultdict

N, d, K, c = tuple(map(int, input().split()))
sushi = list(int(input()) for _ in range(N))
sushi.extend(sushi)

left, right = 0, 0
max_count = 0
eat = defaultdict(int)
eat[c] += 1

for right in range(len(sushi)):
    eat[sushi[right]] += 1

    if right >= K - 1:
        max_count = max(max_count, len(eat))
        eat[sushi[left]] -= 1
        if eat[sushi[left]] == 0:
            del eat[sushi[left]]
        left += 1

print(max_count)

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
