N, M = tuple(map(int, input().split()))
cards = list(map(int, input().split()))
length = len(cards)
answer = 0

for i in range(length - 2):
    for j in range(i + 1, length -1):
        for k in range(j + 1, length):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                answer = max(answer, cards[i] + cards[j] + cards[k])

print(answer)

'''
5 21
5 6 7 8 9
'''
'''
10 500
93 181 245 214 315 36 185 138 216 295
'''
