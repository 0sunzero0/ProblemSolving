from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for length in course:
        # 해당 길이의 combination 구하기
        total_combination = []
        for order in orders:
            combination = combinations(sorted(order), length)
            total_combination += combination

        # 해당 길이의 조합에 대한 count의 큰 값을 구하고, 해당 key를 구하기
        counter = Counter(total_combination)
        if len(counter) != 0 and max(counter.values()) != 1:
            for key in counter:
                if counter[key] == max(counter.values()):
                    answer += [''.join(key) ]

    return sorted(answer)
