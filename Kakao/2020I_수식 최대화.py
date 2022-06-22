import re


def calculate(operator, num1, num2):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == '-':
        return num1 - num2


def solution(expression):
    priorities = [['*', '+', '-'], ['*', '-', '+'],
                  ['+', '*', '-'], ['+', '-', '*'],
                  ['-', '*', '+'], ['-', '+', '*']]

    answer = 0

    for priority in priorities:
        input_operators = re.split('[0-9]+', expression)[1:-1]
        input_operands = re.split('[*+-]', expression)

        for current_operator in priority:
            while current_operator in input_operators:
                idx = input_operators.index(current_operator)
                part_result = calculate(input_operators[idx], int(input_operands[idx]), int(input_operands[idx + 1]))
                del input_operators[idx]
                del input_operands[idx + 1]
                input_operands[idx] = part_result

        result = int(input_operands[0])
        answer = max(abs(result), answer)

    return answer
