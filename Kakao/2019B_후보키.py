def go(idx, element):
    global result

    if idx >= col:
        if len(element) >= 1:
            result.append(set(element))
        return

    element.append(idx)
    go(idx + 1, element)
    element.pop()
    go(idx + 1, element)


def get_all_cases(length):
    global result
    result = list()
    go(0, list())
    return result


def is_uniqueness(key_set):
    return len(key_set) == row


def solution(relation):
    global row, col
    row = len(relation)
    col = len(relation[0])

    superkeys = list()

    # 1. 후보키인지 확인하기 위한 모든 키 경우 구하기
    cases = get_all_cases(col)

    # 2. 유일성 확인
    for case in cases:
        key_set = set()
        for r in range(row):
            key = ""
            for c in case:
                key += (relation[r][c] + " ")
            key_set.add(key)
        if is_uniqueness(key_set):
            superkeys.append(case)

    # 3. 최소성 확인
    answer = 0
    for i in range(len(superkeys)):
        is_minimality = True
        for j in range(len(superkeys)):
            if i != j:
                if superkeys[j] < superkeys[i]:
                    is_minimality = False
        if is_minimality:
            answer += 1

    return answer
