MAX_notation = 36
P, Q = tuple(map(str, input().split()))
answer = []


def change(num, notation):
    result = 0
    power = 0
    for idx in range(len(num) - 1, -1, -1):
        char = num[idx]
        if char.isalpha():
            char = int(ord(char)-87)
        else:
            char = int(char)
        result += char * (notation ** power)
        power += 1

    return result


def is_overflow(num):
    return num > 2 ** 63


def get_min_base(num):
    min_base_num = 2
    for char in num.strip():
        if char.isalpha():
            min_base_num = max(min_base_num, ord(char) - ord('a') + 11)
        else:
            min_base_num = max(min_base_num, ord(char) - ord('0') + 1)

    return min_base_num


def combination():
    min_base_P = get_min_base(P)
    min_base_Q = get_min_base(Q)

    for i in range(min_base_P, MAX_notation + 1):
        for j in range(min_base_Q, MAX_notation + 1):
            notation_P, notation_Q = i, j
            change_P = change(P, notation_P)
            change_Q = change(Q, notation_Q)
            if i != j  and change_P == change_Q:
                X = change_P
                if not is_overflow(X):
                    answer.append([X, notation_P, notation_Q])


def print_answer():
    global answer
    if len(answer) >= 2:
        print("Multiple")
    elif len(answer) == 1:
        print(*answer[0])
    else:
        print("Impossible")


combination()
print_answer()

'''
ep jh
'''
'''
z z
'''
'''
0 0
'''
'''
2222222222222222222222222222222222222222222222222222222222222222222222 8888888888888888888888888888888
'''
