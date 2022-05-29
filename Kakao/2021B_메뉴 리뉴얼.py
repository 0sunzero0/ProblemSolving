hash_map = dict()
selected = []


def get_max_course():
    global hash_map
    result = []

    sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)

    max_value = 2
    for key, value in sorted_hash_map:
        if value >= max_value:
            result.append(key)
            max_value = value

    return result


def combination(current_idx, order, length):
    global hash_map, selected

    if current_idx >= len(order):
        if len(selected) == length:
            key = ''.join(selected)

            if key not in hash_map:
                hash_map[key] = 1
            else:
                hash_map[key] += 1

        return

    selected.append(order[current_idx])
    combination(current_idx + 1, order, length)
    selected.pop()
    combination(current_idx + 1, order, length)


def solution(orders, course):
    global hash_map

    answer = []
    for length in course:
        hash_map = dict()
        for order in orders:
            order = sorted(list(order))

            combination(0, order, length)

        answer += get_max_course()
    return sorted(answer)
