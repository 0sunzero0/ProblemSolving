from collections import deque
import itertools
import copy

# input
N, C = tuple(map(int, input().split()))

# 1 -> 1, 2
person_idx_to_cards_order = deque()
for _ in range(N):
    count, *order = tuple(map(int, input().split()))
    cards_order = deque(order)
    person_idx_to_cards_order.append(cards_order)

# 1 -> ADD a,ADD a,ADD d
card_idx_to_card_calculations = deque()
for _ in range(C):
    calculations = input().split(",")
    card_idx_to_card_calculations.append(calculations)

turn = []
for person_idx, order in enumerate(person_idx_to_cards_order):
    for _ in range(len(order)):
        turn.append(person_idx)

cases = itertools.permutations(turn)


def simulate(case):
    result = ''
    for person_idx in case:
        card_num = temp_person_idx_to_cards_order[person_idx].popleft()

        card_idx = card_num - 1
        calculations = card_idx_to_card_calculations[card_idx]

        for calculation in calculations:
            command, idx = calculation.split(" ")
            if command == "ADD":
                result += idx
            else:
                idx = int(idx)
                if idx >= len(result):
                    return "ERROR"
                result = result[:idx] + result[idx + 1:]

    if len(result) == 0:
        return "EMPTY"

    return result


def print_output():
    for element in sorted(list(set(answer))):
        print(element)


answer = []
for case in cases:
    temp_person_idx_to_cards_order = copy.deepcopy(person_idx_to_cards_order)
    result = simulate(case)
    answer.append(result)

print_output()

'''
2 2
1 1
1 2
ADD a,ADD a,ADD d
DEL 0
'''
'''
2 3
2 1 2
1 3
ADD a
ADD b
ADD c
'''
