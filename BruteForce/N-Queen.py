'''
1. 첫번째 열 n에서 DFS 탐색 시작
2. 다음 열부터, 해당 위치 퀸이 유효한지 검사한다.
    1. 이전 열과 비교
        1. 동일한 대각선 라인에 있으면, → 유효 X
        2. 동일한 가로 및 세로 라인에 있으면 → 유효 X
3. 유효하다면 방문 표시하고, 그 다음 열로 간다.
유효하지 않다면, 다음 행으로 간다.
4. 마지막 열까지 돌면, 탐색 종료, count +=1 해준다.
'''


def attackable(r1, c1, r2, c2):
    # 동일한 행 라인에 있으면 → 유효 X
    if c1 == c2:
        return True
    # 동일한 대각선 라인에 있으면, → 유효 X
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False


def dfs(row, col, n):
    # 4. 마지막 열까지 돌면, 탐색 종료
    if row == n:
        return 1
    else:
        # 2. 해당 열에서 해당 행의 위치가 유효한지 검사한다.
        count = 0
        for cand in range(n):
            possible = True
            # 이전 열과 비교
            for i in range(row):
                if attackable(row, cand, i, col[i]):
                    possible = False
                    break

            if possible:
                # 3. 유효하다면 해당 열의 표시를 하고, 그 다음 열로 간다.
                col[row] = cand
                count += dfs(row + 1, col, n)
        return count


def solution(int):
    col = [0 for _ in range(n)]
    answer = 0
    # 1. 첫번째 열에서 DFS 탐색 시작
    answer += dfs(0, col, n)
    return answer
