'''
1. 문제 설명
정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴
2. 접근 방법 : 어떤 알고리즘인지 
반복문을 사용하여, 반복하는 내용 처리
3. 코드 설명 : 어떻게 코드 짰는지
1) n번 만큼 반복문 사용
2) 반복한 내용 
    x를 증가하고
    x를 리스트에 넣기
4. 느낀점
1) 간단하게 : return [i * x + x for i in range(n)]
'''
def solution(x, n):
    answer = []
    for i in range(0, n):
        #x += x*i
        answer.append(x*(i+1))
    return answer
