# 1. 끝나는 시간이 같은 경우도 있기에, 시작시간도 빠른 기준으로 정렬하자.
# 끝나는 시간, 시작 시간 차례대로 배열을 오름차순 정렬
# 2. 반복문을 돌려서,
# - 차의 끝나는 시간 ≤ 다른 차의 첫시간이면 → 카메라 증가시키기, 최신 카메라위치 = 다른차의 끝시간
# - 그외의 경우는 pass 기존 카메라로 찍힘으로, pass
def solution(routes):
    answer = 1
    routes.sort(key=lambda x : (x[1],x[0]))
    camera_pos = routes[0][1]
    for route in routes:
        if camera_pos < route[0]:
            answer += 1
            camera_pos= route[1]
    return answer
