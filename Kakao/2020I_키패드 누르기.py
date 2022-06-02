hash_map = {1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
            '*': [3, 0], 0: [3, 1], '#': [3, 2]}

left_pos, right_pos = hash_map['*'], hash_map['#']
answer = ''


def get_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


def process_L(number):
    global answer, left_pos
    answer += 'L'
    left_pos = hash_map[number]


def process_R(number):
    global answer, right_pos
    answer += 'R'
    right_pos = hash_map[number]


def solution(numbers, hand):
    global answer, left_pos, right_pos

    for number in numbers:
        if number in (1, 4, 7):
            process_L(number)

        elif number in (3, 6, 9):
            process_R(number)

        else:
            if get_dist(hash_map[number], left_pos) < get_dist(hash_map[number], right_pos):
                process_L(number)
            elif get_dist(hash_map[number], right_pos) < get_dist(hash_map[number], left_pos):
                process_R(number)
            else:
                if hand == "left":
                    process_L(number)
                else:
                    process_R(number)

    return answer
