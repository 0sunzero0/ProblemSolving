def solution(gems):
    gem2cnt = {gems[0]: 1}
    gem_total_cnt = len(set(gems))
    l_idx, r_idx = 0, 0
    answer = [1, len(gems)]

    while l_idx <= r_idx < len(gems):
        if len(gem2cnt) == gem_total_cnt:
            if r_idx - l_idx < answer[1] - answer[0]:
                answer = [l_idx + 1, r_idx + 1]
            gem2cnt[gems[l_idx]] -= 1
            if gem2cnt[gems[l_idx]] == 0:
                del gem2cnt[gems[l_idx]]
            l_idx += 1
        else:
            r_idx += 1
            if r_idx >= len(gems):
                break
            if gems[r_idx] in gem2cnt:
                gem2cnt[gems[r_idx]] += 1
            else:
                gem2cnt[gems[r_idx]] = 1

    return answer
