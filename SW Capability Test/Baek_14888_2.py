from itertools import permutations

N = int(input())
operands = list(map(int, input().split()))
operators_count = list(map(int, input().split()))
operator_type = ['+', '-', '*', '/']
operators = []
max_value = -1000000000
min_value = 1000000000

for i in range(4):
    for _ in range(operators_count[i]):
        operators.append(operator_type[i])

def calculate(operator):
    result = operands[0]
    for i in range(0, len(operator)):
        if operator[i] == '+':
            result += operands[i+1]
        elif operator[i] == '-':
            result -= operands[i+1]
        elif operator[i] == '*':
            result *= operands[i+1]
        elif operator[i] == '/':
            if result < 0 and operands[i+1] > 0:
                result = -((-result) // operands[i + 1])
            else:
                result //= operands[i+1]
    return result

for operator in list(permutations(operators, len(operators))):
    value = calculate(operator)
    max_value = max(value, max_value)
    min_value = min(value, min_value)

print(max_value)
print(min_value)

'''
3
3 4 5
1 0 1 0
'''
'''
7
1 2 3 4 5 6 8
2 2 1 1
'''
