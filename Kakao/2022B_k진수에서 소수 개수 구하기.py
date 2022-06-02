import math


def transfer(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_decimal(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    num = transfer(n, k)

    split_num = num.split("0")

    for element in split_num:
        if element != '' and is_decimal(int(element)):
            answer += 1

    return answer
