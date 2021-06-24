'''
1. 문제 설명
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 
만들 수 있는 모든 수를 
배열에 오름차순으로 담기
2. 접근 방법 : 어떤 알고리즘인지
1) 이중 반복문을 사용해 다 탐색하여 더하기
2) append를 사용해 list에 저장
3) list를 set으로 변환하면, 중복된 것은 저장하지 않는다.
4) sort 사용해 오름차순으로 정렬
3. 코드 설명 : 어떻게 코드 짰는지
1) 반복문 사용해 2개의 수를 뽑는다.
2) 더한 결과를 list에 추가한다. (append 사용)
3) list를 set으로 변환한다.
4) 정렬한다. (sort 사용)
4. 느낀점
1) sorted(list) : 새로운 객체 생성
2) list.sort() : 해당 리스트 자체의 순서를 바꾸는 차이가 있다.
'''
def solution(numbers):
    answer = []
    length = len(numbers)
    sum = 0
    for i in range(0, length):
        for j in range(i+1, length):
            sum = numbers[i] + numbers[j]
            answer.append(sum)
    answer_set = set(answer)
    return sorted(answer_set)
