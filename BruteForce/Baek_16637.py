import re

MIN_INT = -(2 ** 31) - 1
N = int(input())
expression = input()
operators = re.split('[0-9]', expression)[1:-1]
operands = re.split('[*+-]', expression)
operands = [int(element) for element in operands]


def calculate(num1, num2, operator):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == '-':
        return num1 - num2


def go(current_idx, value):
    global answer
    if current_idx == len(operands):
        answer = max(answer, value)
        return

    # 괄호 없이 계산한 경우
    go(current_idx + 1, calculate(value, operands[current_idx], operators[current_idx - 1]))
    # 괄호가 있는 경우
    if current_idx + 2 <= len(operands):
        go(current_idx + 2, calculate(value, calculate(operands[current_idx], operands[current_idx + 1], operators[current_idx]), operators[current_idx - 1]))


answer = MIN_INT
go(1, operands[0])
print(answer)

'''
9
3+8*7-9*2
'''
