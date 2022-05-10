def solution(gems):
    gems_dict = {gems[0]: 1}
    gems_kind = len(set(gems))
    gems_length = len(gems)

    answer = [1, len(gems)]
    left, right = 0, 0

    while left <= right and right < gems_length:
        if len(gems_dict) == gems_kind:
            if right - left < answer[1] - answer[0]:
                answer = [left + 1, right + 1]

            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
            left += 1

        elif len(gems_dict) < gems_kind:
            right += 1
            if right >= gems_length:
                break

            if gems[right] not in gems_dict:
                gems_dict[gems[right]] = 1
            else:
                gems_dict[gems[right]] += 1

    return answer
