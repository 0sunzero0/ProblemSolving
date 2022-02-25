'''
- 입력값을 받아 딕셔너리에 저장
- 각 의상의 종류의 갯수를 다 곱한다.
    How? 각 경우를 다 곱해주면 된다. 각 의상의 종류별로 아무것도 안 입는 경우가 있으니 +1 한다.
    또한 모두 안 입는 경우는 없다고 했으니 최종 곱한 값 -1 하기
'''


def solution(clothes):
    closet = {}
    result = 1

    for clothe in clothes:
        key = clothe[1]
        value = clothe[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    for key, value in closet.items():
        result *= len(value) + 1
    result -= 1
    return result
