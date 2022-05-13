N, M = tuple(map(int, input().split()))
cards = list(map(int, input().split()))

selected_cards = []
min_diff = 300000 - 3 * 1
answer = 0


def choose(curr_idx):
    global min_diff, answer
    current_sum = sum(selected_cards)
    current_length = len(selected_cards)

    if current_sum > M or current_length > 3:
        return

    if curr_idx == len(cards):
        if current_length == 3:
            current_diff = M - current_sum
            if current_diff < min_diff:
                min_diff = min(current_diff, min_diff)
                answer = current_sum
        return

    selected_cards.append(cards[curr_idx])
    choose(curr_idx + 1)
    selected_cards.pop()
    choose(curr_idx + 1)


choose(0)
print(answer)

'''
5 21
5 6 7 8 9
'''
'''
10 500
93 181 245 214 315 36 185 138 216 295
'''
'''
3 20
1 1 1
'''
