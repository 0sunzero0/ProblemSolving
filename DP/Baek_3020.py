MAX_INT = 500000
N, H = tuple(map(int, input().split()))
top = [0] * (H + 1) # 종유석
bottom = [0] * (H + 1)  # 석순
min_count = MAX_INT
answer = []

for i in range(N):
    num = int(input())
    if i % 2:
        top[num] += 1
    else:
        bottom[H - num + 1] += 1

# 종유석은 위에서부터 아래로
for i in range(H - 1, 0, -1):
    top[i] += top[i + 1]
# 석순은 아래에서부터 위로
for i in range(1, H):
    bottom[i + 1] += bottom[i]

for i in range(1, H + 1):
    count = top[i] + bottom[i]
    if count < min_count:
        min_count = count
        answer = [i]
    elif count == min_count:
        answer.append(i)

print(min_count, len(answer))

'''
6 7
1
5
3
3
5
1
'''
'''
14 5
1
3
4
2
2
4
3
4
3
3
3
2
3
3
'''
