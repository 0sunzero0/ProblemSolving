from itertools import permutations


def check(case, banned_id):
    for idx in range(len(banned_id)):
        if len(case[idx]) != len(banned_id[idx]):
            return False

        for j in range(len(case[idx])):
            if banned_id[idx][j] == "*":
                continue
            if banned_id[idx][j] != case[idx][j]:
                return False

    return True


def solution(user_id, banned_id):
    cases = list(permutations(user_id, len(banned_id)))
    banned_set = set()

    for case in cases:
        if not check(case, banned_id):
            continue
        else:
            case = set(case)
            if case not in banned_set:
                banned_set.add(case)

    return len(banned_set)
