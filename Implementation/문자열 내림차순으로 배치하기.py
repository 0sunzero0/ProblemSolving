'''
1. 문제 설명
문자열 큰 것부터 작은 것 순으로 정렬해 새로운 문자열 리턴 단, 대문자는 소문자보다 작다.
2. 접근 방법 : 어떤 알고리즘인지 
1) sorted 함수 reverse = True
2) ""join
3. 느낀점
1) ""join을 통해 리스트를 문자열로 바꿀 수 있다.
'''

def solution(s):
    return ("".join(sorted(s, reverse = True)))
