def init():
    N = int(input())
    order = list()
    student_like = dict()
    student_pos = dict()

    for _ in range(N * N):
        students = tuple(map(int, input().split()))
        cur_student, like_students = students[0], students[1:5]
        order.append(cur_student)
        student_like[cur_student] = like_students

    return N, order, student_like, student_pos


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def place(cur_student):
    mark = [[0] * N for _ in range(N)]
    like_students = student_like[cur_student]

    # 1. 1번 조건 확인
    cond1_pos = list()
    for like_student in like_students:
        if like_student not in student_pos:
            continue
        r, c = student_pos[like_student]
        for d in range(4):
            nr, nc = r + dys[d], c + dxs[d]
            if in_range(nr, nc) and not shark_class[nr][nc]:
                mark[nr][nc] += 1
    max_value = max(map(max, mark))
    for r in range(N):
        for c in range(N):
            if mark[r][c] == max_value:
                cond1_pos.append((r, c))

    # 2. 2, 3번 조건 확인
    side_count_and_pos = list()
    for pos in cond1_pos:
        r, c = pos
        count = 0
        for d in range(4):
            nr, nc = r + dys[d], c + dxs[d]
            if in_range(nr, nc) and not shark_class[nr][nc]:
                count += 1
        side_count_and_pos.append((count, r, c))

    # count, r, c 기준으로 정렬
    side_count_and_pos.sort(key=lambda x: (-x[0], x[1], x[2]))

    # 3. 해당 자리가 비어있다면 자리에 앉히기
    for element in side_count_and_pos:
        _, final_r, final_c = element
        if shark_class[final_r][final_c] == 0:
            shark_class[final_r][final_c] = cur_student
            student_pos[cur_student] = (final_r, final_c)
            break


def simulate():
    for cur_student in order:
        place(cur_student)


def count2satisfaction(cur_count):
    if cur_count == 0:
        return 0
    return 10 ** (cur_count - 1)


def get_satisfaction():
    total_satisfaction = 0
    for r in range(N):
        for c in range(N):
            cur_student = shark_class[r][c]
            cur_count = 0
            for d in range(4):
                nr, nc = r + dys[d], c + dxs[d]
                if in_range(nr, nc):
                    side_student = shark_class[nr][nc]
                    if side_student in student_like[cur_student]:
                        cur_count += 1
            cur_satisfaction = count2satisfaction(cur_count)
            total_satisfaction += cur_satisfaction

    return total_satisfaction


N, order, student_like, student_pos = init()
dys = [-1, 0, 1, 0]
dxs = [0, -1, 0, 1]
shark_class = [[0] * N for _ in range(N)]

simulate()
print(get_satisfaction())

'''
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
'''
