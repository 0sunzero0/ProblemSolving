'''
1. 문제 설명
번호가 증가하는 순서대로 1초 동안 음식을 먹음.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식부터
k초 후 먹기 시작할 음식 번호는 무엇인지 return
- 입력 :
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 
네트워크 장애가 발생한 시간 K 초
- 출력 :
몇 번 음식부터 다시 섭취하면 되는지 return

2. 어떤 알고리즘인지
Greedy
이 문제는 시간이 적게 걸리는 음식부터 확인하는 Greedy 접근 방식으로 해결
모든 음식을 시간을 기준으로 정렬한 뒤에 시간이 적게 걸리는 음식부터 제거해 나가는 방식
- 우선순위 큐 사용

3. 어떻게 코드로 구현했는지
1)
- 모든 음식을 우선순위 큐(최소 힙)에 삽입
- 마지막에는 k초 후에 먹어야 할 음식의 번호를 출력해야 하므로 우선순위 큐에 삽입할 때
(음식 시간, 음식 번호)의 튜플 형태로 삽입
2) 가장 적게걸리는 음식을 빼기    
3) 다음으로 적게 걸리는 음식 빼기
정당성 체크 : 남은 시간보다 작음 -> 따라서 당므으로 먹어야 할 음식의 번호를 찾아 출력

4. 느낀점
1) 최고의 것을 선택해서 해결하는 아이디어가 필요
'''

import heapq

def solution(food_times, k):
    if sum(food_times) <= k :    return -1
    
    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # 음식 시간, 음식 번호 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous =  0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수와 k 비교
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수
    # 와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x:x[1]) # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]
