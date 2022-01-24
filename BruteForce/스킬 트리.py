'''
- skill_tree를 순회 (각 skill_tree에 skill 하나 가져오기)
    - skill을 순회
        - 해당 skill의 하나의 element가 skill 리스트에 있다면,
            - 스킬 리스트의 남은 skill 중 맨 앞과 같은지 확인
                - 맨 앞과 같다면, pop 한다.
                - 아니라면, → flag = false
        - 다 순회하고, flag == true면 count += 1
'''


def solution(skill, skill_trees):
    count = 0

    # skill_tree를 순회 (각 skill_tree에 skill 하나 가져오기)
    for skills in skill_trees:
        # skill을 순회
        # skill 리스트로 변환하자.
        skill_standard = list(skill)
        flag = True

        for element in skills:
            # 해당 skill의 하나의 element가 skill 리스트에 있다면,
            if element in skill_standard:
                # 스킬 리스트의 남은 skill 중 맨 앞과 다른지 확인
                if element != skill_standard.pop(0):
                    flag = False

        # 다 순회하고, count += 1
        if flag == True:
            count += 1

    return count