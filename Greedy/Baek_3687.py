N = int(input())

count_to_min_default = {2: 1, 3: 7, 4: 4, 5: 2, 6: 6, 7: 8, 8: 10, 9: 18, 10: 22}


def get_big(count):
    if count % 2 == 0:
        result = '1' * (count // 2)
    else:
        result = '7' + '1' * ((count - 3) // 2)
    return int(result)


def get_small(count):
    if count < 11:
        return count_to_min_default[count]

    result = [8 for _ in range((count + 6) // 7)]
    if count % 7 == 1:
        result[0], result[1] = 1, 0
    elif count % 7 == 2:
        result[0] = 1
    elif count % 7 == 3:
        result[0], result[1], result[2] = 2, 0, 0
    elif count % 7 == 4:
        result[0], result[1] = 2, 0
    elif count % 7 == 5:
        result[0] = 2
    elif count % 7 == 6:
        result[0] = 6

    result = ''.join(str(element) for element in result)
    return int(result)


for _ in range(N):
    Q = int(input())
    biggest = get_big(Q)
    smallest = get_small(Q)
    print(smallest, biggest)

'''
4
3
6
7
15
'''
