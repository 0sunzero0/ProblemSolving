def init():
    m, bc_cnt = tuple(map(int, input().split()))
    user1_info = tuple(map(int, input().split()))
    user2_info = tuple(map(int, input().split()))
    bc_info = dict()
    for bc_num in range(1, bc_cnt + 1):
        c, r, dist, p = tuple(map(int, input().split()))
        bc_info[bc_num] = [(r - 1, c - 1), dist, p]

    return m, bc_cnt, user1_info, user2_info, bc_info


def make_ap_area():
    grid = [
        [list() for _ in range(N)]
        for _ in range(N)
    ]

    for key, value in BC_info.items():
        pos, dist, p = value
        r, c = pos
        for i in range(N):
            for j in range(N):
                if abs(r - i) + abs(c - j) <= dist:
                    grid[i][j].append(key)

    return grid


def calculate_charge(user1_selected_ap_num, user2_selected_ap_num):
    result = 0

    count = [0] * (BC_cnt + 1)
    count[user1_selected_ap_num] += 1
    count[user2_selected_ap_num] += 1

    _, _, p1 = BC_info[user1_selected_ap_num]
    _, _, p2 = BC_info[user2_selected_ap_num]

    result += p1 // count[user1_selected_ap_num]
    result += p2 // count[user2_selected_ap_num]

    return result


def get_max_data():
    global userA_r, userA_c, userB_r, userB_c
    result = 0
    user1_all_ap_num = ap[userA_r][userA_c]
    user2_all_ap_num = ap[userB_r][userB_c]

    if len(user1_all_ap_num) == 0:
        for user2_selected_ap_num in user2_all_ap_num:
            _, _, p2 = BC_info[user2_selected_ap_num]
            result = max(result, p2)
    elif len(user2_all_ap_num) == 0:
        for user1_selected_ap_num in user1_all_ap_num:
            _, _, p1 = BC_info[user1_selected_ap_num]
            result = max(result, p1)
    else:
        for user1_selected_ap_num in user1_all_ap_num:
            for user2_selected_ap_num in user2_all_ap_num:
                result = max(result, calculate_charge(user1_selected_ap_num, user2_selected_ap_num))
    return result


def move_next_pos(i):
    global userA_r, userA_c, userB_r, userB_c
    userA_r += drs[userA_info[i]]
    userA_c += dcs[userA_info[i]]
    userB_r += drs[userB_info[i]]
    userB_c += dcs[userB_info[i]]


def print_ap():
    for i in range(N):
        for j in range(N):
            print(ap[i][j], end=" ")
        print()


drs = [0, -1, 0, 1, 0]
dcs = [0, 0, 1, 0, -1]


T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    N = 10
    userA_r, userA_c, userB_r, userB_c = 0, 0, N - 1, N - 1

    total_move_time, BC_cnt, userA_info, userB_info, BC_info = init()
    ap = make_ap_area()
    # print_ap()
    for idx in range(total_move_time):
        answer += get_max_data()
        move_next_pos(idx)
    answer += get_max_data()

    print(f"#{test_case} {answer}")

'''
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
'''
'''
5
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
40 2
0 3 0 3 3 2 2 1 0 4 1 3 3 3 0 3 4 1 1 3 2 2 2 2 2 0 2 3 2 2 3 4 4 3 3 3 2 0 4 4 
0 1 0 3 4 0 4 0 0 1 1 1 0 1 4 4 4 4 4 3 3 3 0 1 0 4 3 2 1 4 4 3 2 3 2 2 0 4 2 1 
5 2 4 140
8 3 3 490
60 4
0 3 3 3 0 1 2 2 2 1 2 2 3 3 4 4 0 3 0 1 1 2 2 3 2 2 3 2 2 0 3 0 1 1 1 4 1 2 3 3 3 3 3 1 1 4 3 2 0 4 4 4 3 4 0 3 3 0 3 4 
1 1 4 1 1 1 1 1 1 4 4 1 2 2 3 2 4 0 0 0 4 3 3 4 3 3 0 1 0 4 3 0 4 3 2 3 2 1 2 2 3 4 0 2 2 1 0 0 1 3 3 1 4 4 3 0 1 1 1 1 
6 9 1 180
9 3 4 260
1 4 1 500
1 3 1 230
80 7
2 2 2 2 2 2 0 2 2 0 4 0 2 3 3 2 3 3 0 3 3 3 4 3 3 2 1 1 1 0 4 4 4 1 0 2 2 2 1 1 4 1 2 3 4 4 3 0 1 1 0 3 4 0 1 2 2 2 1 1 3 4 4 4 4 4 4 3 2 1 4 4 4 4 3 3 3 0 3 3 
4 4 1 1 2 1 2 3 3 3 4 4 4 4 4 1 1 1 1 1 1 1 1 0 3 3 2 0 4 0 1 3 3 3 2 2 1 0 3 2 3 4 1 0 1 2 2 3 2 0 4 0 3 4 1 1 0 0 3 2 0 0 4 3 3 4 0 4 4 4 4 0 3 0 1 1 4 4 3 0 
4 3 1 170
10 1 3 240
10 5 3 360
10 9 3 350
9 6 2 10
5 1 4 350
1 8 2 450
100 8
2 2 3 2 0 2 0 3 3 1 2 2 2 2 3 3 0 4 4 3 2 3 4 3 3 2 3 4 4 4 2 2 2 0 2 2 4 4 4 4 1 1 1 2 2 2 4 3 0 2 3 3 4 0 0 1 1 4 1 1 1 1 2 2 1 1 3 3 3 0 3 2 3 3 0 1 3 3 0 1 1 3 3 4 0 4 1 1 2 2 4 0 4 1 1 2 2 1 1 1 
4 4 4 0 4 1 1 4 1 1 1 1 3 2 1 2 1 1 4 4 1 0 2 3 4 4 4 4 4 0 1 0 2 2 2 0 2 2 2 2 2 2 3 0 0 1 4 3 3 2 0 0 4 4 4 0 2 0 4 1 1 2 2 0 4 4 0 0 2 0 2 3 3 0 2 3 0 3 4 0 4 3 4 4 3 4 1 1 2 2 2 0 0 1 0 4 1 1 1 4 
3 4 2 340
10 1 1 430
3 10 4 10
6 3 4 400
7 4 1 80
4 5 1 420
4 1 2 350
8 4 4 300
'''
