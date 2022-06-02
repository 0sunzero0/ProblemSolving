max_diff = 0
answer = []


def go(info, shoot, n, i):
    global answer, max_diff

    if i == 11:
        if n != 0:
            shoot[10] = n

        score_diff = calculate_diff(info, shoot)

        if score_diff <= 0:
            return

        result = shoot[::]
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [result]
            return

        if score_diff == max_diff:
            answer.append(result)
        return

    # 점수 먹는 경우
    if info[i] < n:
        shoot.append(info[i] + 1)
        go(info, shoot, n - info[i] - 1, i + 1)
        shoot.pop()

    # 점수 안 먹는 경우
    shoot.append(0)
    go(info, shoot, n, i + 1)
    shoot.pop()


def calculate_diff(info, shoot):
    peach_score, ryan_score = 0, 0
    for i in range(11):
        if (info[i], shoot[i]) == (0, 0):
            continue
        if info[i] >= shoot[i]:
            peach_score += (10 - i)
        else:
            ryan_score += (10 - i)

    return ryan_score - peach_score


def solution(n, info):
    global answer, max_diff
    go(info, [], n, 0)

    if len(answer) == 0:
        return [-1]

    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
