import math


def is_prime_number(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def go(current_number):
    if not is_prime_number(int(current_number)):
        return

    if len(current_number) == N:
        answer.append(int(current_number))
        return

    for num in odd_number:
        current_number = current_number + num
        go(current_number)
        current_number = current_number[:-1]


answer = []
N = int(input())
start = ['2', '3', '5', '7']
odd_number = ['1', '3', '5', '7', '9']

for element in start:
    go(element)

answer.sort()
for element in answer:
    print(element)
