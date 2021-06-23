'''
1. 문제 설명
1,2,3번 수포자 찍는 방식 고정
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return

2. 접근 방법 : 어떤 알고리즘인지 
1번 수포자 1, 2, 3, 4, 5 반복 (길이 : 5)
2번 수포자 2, 1, 2, 3, 2, 4, 2, 5 반복 (길이 : 8)
3번 수포자 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복 (길이 : 10)

1) 반복문해서 비교 (0~정답문의 길이까지)
수포자 1,2,3 같이 비교
정답[i] == 수포자 배열 [i%수포자 배열의 길이]
정답이 맞으면 count 추가
2) 수포자 1,2,3의 count 리스트에 저장
3) count의 max 구하기
4) 반복문 돌려서 count의 max와 일치되는 count의 index를 리스트에 추가하고 최종 리스트 리턴

3. 코드 설명 : 어떻게 코드 짰는지
1) 각자 수포자 찍는 방식 배열에 저장
2) 반복문해서 비교 (0~정답문의 길이까지)
수포자 1,2,3 같이 비교
정답[i] == 수포자 배열 [i%수포자 배열의 길이]
count{num} += 1
3) count1, count2, count3 리스트에 넣기 변수명 : count_list
4) max = count 중 제일 큰 숫자 (이때, max 함수 사용)
5) 반복문 돌려서 index와 score 변수(count list로 부터 가져오는 변수) 설정 
count1, count2, count3 비교하여 max와 일치된 index 정답 리스트에 추가

4. 느낀점
enumerate
'''
def solution(answers):
    check1 = [1, 2, 3, 4, 5]
    check2 = [2, 1, 2, 3, 2, 4, 2, 5]
    check3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for i in range(0, len(answers)):
        if(answers[i] == check1[i%len(check1)]):
            count[0] += 1
        if(answers[i] == check2[i%len(check2)]):
            count[1] += 1
        if(answers[i] == check3[i%len(check3)]):
            count[2] += 1
    
    max_count = max(count)
    answer_list = []
    
    for index, score in enumerate(count):
        if score == max_count:
            answer_list.append(index+1)
    return answer_list
