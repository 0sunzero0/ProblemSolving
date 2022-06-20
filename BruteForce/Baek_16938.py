N, L, R, X = tuple(map(int, input().split()))
levels = list(map(int, input().split()))
selected_levels = []
answer = 0


def is_ok():
    return len(selected_levels) >= 2 and max(selected_levels) - min(selected_levels) >= X and L <= sum(selected_levels) <= R


def combination(current_idx):
    global answer
    if current_idx == len(levels):
        if is_ok():
            answer += 1
        return

    selected_levels.append(levels[current_idx])
    combination(current_idx + 1)
    selected_levels.pop()
    combination(current_idx + 1)


combination(0)
print(answer)
'''
3 5 6 1
1 2 3
'''
'''
4 40 50 10
10 20 30 25
'''
'''
5 25 35 10
10 10 20 10 20
'''
