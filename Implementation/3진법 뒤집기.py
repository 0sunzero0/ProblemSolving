'''
1. 문제 설명
1) n을 3진법 
2) 앞뒤로 뒤집은 후,  
3) 다시 10진법으로 표현한 수를 return

2. 알고리즘 
1) n을 3진법으로 + 뒤집기
- 반복적으로 n % 3 -> 문자열에 넣기

2) 3진법 10진수
- 문자열 길이 구하기
- 반복할 조건 index~문자열 길이 만큼
- 반복할 내용 answer += 문자열(index) * exp(3, len-1-index)

3. 느낀점
n진수 → 10진수 함수가 있다.
int(string, base)
'''
def solution(n):
    num = n
    string = ''
    while(1):
        if(num == 0):   break
        string += str(num % 3)
        num = num // 3
    
    answer = 0
    for index in range(len(string)):
        answer += int(string[index]) * (3 ** (len(string)-1-index))
    
    return answer
