from collections import defaultdict


def solution(info, query):
    # 데이터 HashMap에 저장
    condition2scores = defaultdict(list)

    for one_info in info:
        language, field, career, food, score = one_info.split(" ")
        for first in (language, "-"):
            for second in (field, "-"):
                for third in (career, "-"):
                    for fourth in (food, "-"):
                        condition = first + " " + second + " " + third + " " + fourth
                        condition2scores[condition].append(int(score))

    for condition, scores in condition2scores.items():
        condition2scores[condition] = sorted(scores)

    # 각 쿼리마다 데이터의 개수 찾기
    answer = []

    for one_query in query:
        language, field, career, food_and_score = one_query.split(" and ")
        food, score = food_and_score.split(" ")

        condition = language + " " + field + " " + career + " " + food
        count = get_lower_bound(condition2scores[condition], int(score))
        answer.append(count)
    return answer


def get_lower_bound(scores, standard):
    N = len(scores)
    left, right, min_idx = 0, N - 1, N

    while left <= right:
        mid = (left + right) // 2
        if scores[mid] >= standard:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1

    return N - min_idx
