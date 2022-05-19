N = int(input())
requests = []

for _ in range(N):
    requests.append(tuple(map(int, input().split())))

requests.sort(key=lambda x:(x[1], x[0]))

last_end, answer = -1, 0
for start, end in requests:
    if last_end <= start:
        last_end = end
        answer += 1

print(answer)

'''
12
1 4
3 5
0 6
4 7
7 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
