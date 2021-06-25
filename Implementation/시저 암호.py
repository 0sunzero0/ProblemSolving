'''
느낀점
1. 함수 라이브러리 활용 잘하기(검색해보고 사용하기)
2. "".join(s) : s라는 리스트를 string으로 바꿔준다.
3. z 벗어나는 문제 -> 나머지를 구해주는 함수를 사용하자.
'''
def solution(s, n):
    s = list(s) 
    for i in range(len(s)): 
        if s[i].isupper(): 
            s[i]=chr((ord(s[i])-ord('A')+ n)%26 + ord('A')) 
        elif s[i].islower(): 
            s[i]=chr((ord(s[i])-ord('a')+ n)%26 + ord('a')) 
    
    return "".join(s)
