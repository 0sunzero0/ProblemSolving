from collections import defaultdict
import math


def calculate_fee(fees, total_time):
    if total_time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]


def calculate_time(in_time, out_time):
    inHH, inMM = in_time.split(":")
    outHH, outMM = out_time.split(":")
    return (int(outHH) * 60 + int(outMM)) - (int(inHH) * 60 + int(inMM))


def solution(fees, records):
    carnum_to_intime = defaultdict(int)
    carnum_to_totaltime = defaultdict(int)
    carnum_to_fee = defaultdict(int)

    # 1. 차량별 누적 시간 구하기
    for record in records:
        time, car_num, details = record.split(" ")
        if details == "IN":
            carnum_to_intime[car_num] = time
        else:
            in_time = carnum_to_intime.pop(car_num)
            total_time = calculate_time(in_time, time)
            carnum_to_totaltime[car_num] += total_time

    for car_num, in_time in carnum_to_intime.items():
        total_time = calculate_time(in_time, "23:59")
        carnum_to_totaltime[car_num] += total_time

    # 2. 차량별 요금 구하기
    for car_num, total_time in carnum_to_totaltime.items():
        current_fee = calculate_fee(fees, total_time)
        carnum_to_fee[car_num] += current_fee

    sorted_carnum_to_fee = sorted(carnum_to_fee.items(), key=lambda item: item[0])
    sorted_fee_by_carnum = [element[1] for element in sorted_carnum_to_fee]

    return sorted_fee_by_carnum
