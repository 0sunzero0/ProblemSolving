def is_right(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:   return False
            stack.pop()

    return True


def divide_two_blanced(p):
    left_count = 0
    right_count = 0

    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:   return p[:i + 1], p[i + 1:]


def solution(p):
    # 1.  입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if len(p) == 0:
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u, v = divide_two_blanced(p)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if is_right(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer = '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다.
        answer += ')'
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:-1]
        for element in u:
            if element == ')':
                answer += '('
            else:
                answer += ')'
        # 4-5. 생성된 문자열을 반환합니다.
        return answer
