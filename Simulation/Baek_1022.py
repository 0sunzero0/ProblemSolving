r1, c1, r2, c2 = tuple(map(int, input().split()))
spiral_points = []


def search_spiral():
    dys = [0, -1, 0, 1]
    dxs = [1, 0, -1, 0]
    curr_y, curr_x = 0, 0
    move_dir, move_step = 0, 1
    value, max_print_value = 1, 1

    max_border = max([abs(r1), abs(c1), abs(r2), abs(c2)])

    if r1 <= curr_y <= r2 and c1 <= curr_x <= c2:
        spiral_points.append((curr_y, curr_x, value))

    while -max_border <= curr_y <= max_border or -max_border <= curr_x <= max_border:
        for _ in range(move_step):
            curr_y += dys[move_dir]
            curr_x += dxs[move_dir]
            value += 1

            if r1 <= curr_y <= r2 and c1 <= curr_x <= c2:
                spiral_points.append((curr_y, curr_x, value))
                max_print_value = max(max_print_value, value)

        move_dir = (move_dir + 1) % 4

        if move_dir == 0 or move_dir == 2:
            move_step += 1

    return max_print_value


def get_length(value):
    return len(str(value))


def print_answer():
    spiral_points.sort(key=lambda x: (x[0], x[1]))
    for element in spiral_points:
        curr_y, curr_x, value = element
        current_length = len(str(value))
        print(' ' * (max_length - current_length) + str(value), end=" ")

        if curr_x == c2:
            print()


max_print_value = search_spiral()
max_length = get_length(max_print_value)
print_answer()

'''
-3 -3 2 0
'''
'''
-2 2 0 3
'''
