def step1(id):
    return id.lower()


def step2(id):
    result = ''
    for word in id:
        if word.isalnum() or word in '-_.':
            result += word
    return result


def step3(id):
    while '..' in id:
        id = id.replace('..', '.')
    return id


def step4(id):
    if id[0] == '.' and len(id) > 1:
        id = id[1:]
    if id[-1] == '.':
        id = id[:-1]
    return id


def step5(id):
    if id == '':
        id = 'a'
    return id


def step6(id):
    if len(id) >= 16:
        id = id[0:15]
        if id[-1] == '.':
            id = id[:-1]
    return id


def step7(id):
    if len(id) <= 2:
        while len(id) < 3:
            id += id[-1]
    return id


def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id
