def solution(clothes):
    closet = {}
    result = 1

    for clothe in clothes:
        key = clothe[1]
        value = clothe[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    for key, value in closet.items():
        result *= len(value) + 1
    result -= 1
    return result
