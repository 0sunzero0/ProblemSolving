'''
코드 설명
1) len 받기
2) length-4 길이만큼 * 표시 + phone_number 뒤에서 4자리까지 표시
'''
def solution(phone_number):
    length = len(phone_number)
    answer = "*"*(length-4) + phone_number[-4:]
    
    return answer
