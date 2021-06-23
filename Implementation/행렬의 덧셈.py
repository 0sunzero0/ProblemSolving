'''
1. 문제 설명
2개의 행렬을 덧셈하는 문제다.
이때, 2개의 행렬은 행과 열의 크기가 같다.

2. 접근 방법 : 어떤 알고리즘인지 
1) 행과 열의 갯수를 구하고
2) 중첩 반복문 사용하여 각각의 행과 열에 따라 두개의 값을 더한다.

3. 코드 설명 : 어떻게 코드 짰는지
1) row, col 길이 받기
2) answer에 임의의 값 생성
3) 중첩 반복문 써서 각각의 행렬의 값에 접근해 더하기

4. 느낀점
1) 굳이 answer라는 리스트를 따로 만들어 생성할 필요가 있었을까?
2) numpy library 쓰면 더 쉽게 간단히 구현 가능
'''
def solution(arr1, arr2):
    row_len = len(arr1)
    col_len = len(arr1[0])
    answer = [[0]*col_len for i in range(row_len)] 
    
    for i in range(0, row_len):
        for j in range(0, col_len):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
