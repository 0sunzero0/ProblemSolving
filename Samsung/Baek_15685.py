def in_range(x, y):
    return 0 <= x <= 100 and 0 <= y <= 100


def get_dragon_curve_dir(d, g):
    # 0세대
    result = [d]

    # 1 ~ g세대
    for _ in range(g):
        reverse_result = reversed(result)
        for d in reverse_result:
            result.append((d + 1) % 4)

    return result


def draw_dragon_curve(sx, sy, dragon_curve_dir):
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    paper[sy][sx] = True
    cx, cy = sx, sy

    for curr_dir in dragon_curve_dir:
        cx += dxs[curr_dir]
        cy += dys[curr_dir]

        if in_range(cx, cy):
            paper[cy][cx] = True


def simulate():
    N = int(input())
    for _ in range(N):
        x, y, d, g = tuple(map(int, input().split()))
        dragon_curve_dir = get_dragon_curve_dir(d, g)
        draw_dragon_curve(x, y, dragon_curve_dir)


def get_answer():
    answer = 0
    for r in range(PAPER_SIZE):
        for c in range(PAPER_SIZE):
            if paper[r][c] and paper[r][c + 1] and paper[r + 1][c] and paper[r + 1][c + 1]:
                answer += 1
    return answer


def print_paper():
    for r in range(PAPER_SIZE):
        for c in range(PAPER_SIZE):
            if paper[r][c]:
                print(r, c)


PAPER_SIZE = 100
paper = [[False] * (PAPER_SIZE + 1) for _ in range(PAPER_SIZE + 1)]
simulate()
print(get_answer())

'''
3
3 3 0 1
4 2 1 3
4 2 2 1
'''
'''
4
3 3 0 1
4 2 1 3
4 2 2 1
2 7 3 4
'''
