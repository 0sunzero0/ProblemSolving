def go(month, cost):
    global min_pay
    if month > 12:
        min_pay = min(min_pay, cost)
        return

    if plans[month] == 0:
        go(month + 1, cost)
    go(month + 1, cost + price[0] * plans[month])
    go(month + 1, cost + price[1])
    go(month + 3, cost + price[2])
    go(month + 12, cost + price[3])


def init():
    price = list(map(int, input().split()))
    plans = [0] + list(map(int, input().split()))
    return price, plans


test_case_num = int(input())

for simulation_count in range(1, test_case_num + 1):
    price, plans = init()
    min_pay = 3000 * 31 * 12
    go(1, 0)
    print("#" + str(simulation_count) + " " + str(min_pay))


'''
10
10 40 100 300
0 0 2 9 1 5 0 0 0 0 0 0
10 100 50 300
0 0 0 0 0 0 0 0 6 2 7 8
10 70 180 400
6 9 7 7 7 5 5 0 0 0 0 0
10 70 200 550
0 0 0 0 8 9 6 9 6 9 8 6
10 80 200 550
0 8 9 15 1 13 2 4 9 0 0 0
10 130 360 1200
0 0 0 15 14 11 15 13 12 15 10 15
10 180 520 1900
0 18 16 16 19 19 18 18 15 16 17 16
10 100 200 1060
12 9 11 13 11 8 6 12 8 7 15 6
10 170 500 1980
19 18 18 17 15 19 19 16 19 15 17 18
10 200 580 2320
12 28 24 24 29 25 23 26 26 28 27 22
'''
