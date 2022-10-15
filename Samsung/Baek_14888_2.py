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
            if result < 0 and operands[i + 1] > 0:
                result = -((-result) // operands[i + 1])
            else:
                result //= operands[i + 1]
    return result


selected = []
visited = [False] * (N - 1)


def permutation(depth):
    global max_value, min_value
    if depth == N - 1:
        if len(selected) == N - 1:
            max_value = max(max_value, calculate(selected))
            min_value = min(min_value, calculate(selected))
        return

    for i in range(N - 1):
        if not visited[i]:
            visited[i] = True
            selected.append(operators[i])

            permutation(depth + 1)

            visited[i] = False
            selected.pop()


permutation(0)
print(max_value)
print(min_value)

'''
6
1 2 3 4 5 6
2 1 1 1
'''
