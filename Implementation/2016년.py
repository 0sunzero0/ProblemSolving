'''
느낀점
1) 자료구조 활용을 잘하는 것이 중요하다.
2) sum을 활용해 리스트의 합을 쉽게 구할 수 있다.
ex. 
    return days[(sum(months[:a-1])+b-1)%7]
'''
def solution(a, b):
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    dayNum = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0

    for i in range(a):
        count += dayNum[i]
    count += b
        
    return days[count % 7]
