N = int(input())
operands = list(map(int, input().split()))
operators_count = list(map(int, input().split()))
operator_type = ['+', '-', '*', '/']
max_value = -1000000000
min_value = 1000000000

def calculator(operand1, candidate, operand2):
    if operator_type[candidate] == '+':
        result = operand1 + operand2
    elif operator_type[candidate] == '-':
        result = operand1 - operand2
    elif operator_type[candidate] == '*':
        result = operand1 * operand2
    elif operator_type[candidate] == '/':
        if operand1 < 0 and operand2 > 0:
            result = -((-operand1) // operand2)
        else:
            result = operand1 // operand2
    return result

def calculate(index, result):
    global min_value, max_value
    if index == N-1:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
    else:
        global operators_count
        for candidate in range(4):
            if operators_count[candidate] >= 1:
                operators_count[candidate] -= 1
                calculate(index + 1, calculator(result, candidate, operands[index + 1]))
                operators_count[candidate] += 1

calculate(0, operands[0])
print(max_value)
print(min_value)
