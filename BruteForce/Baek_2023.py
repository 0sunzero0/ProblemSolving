import math


def is_prime_number(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def go(current_digit):
    global current_number
    if not len(current_number) == 0 and not is_prime_number(int(current_number)):
        return

    if current_digit == N + 1:
        if len(current_number) == N:
            answer.append(int(current_number))
        return

    for num in range(1, 10):
        if current_digit == N:
            if num == 0:
                continue
        current_number = current_number + str(num)
        go(current_digit + 1)
        current_number = current_number[:-1]


answer = []
N = int(input())
current_number = ''

go(1)
answer.sort()
for element in answer:
    print(element)
