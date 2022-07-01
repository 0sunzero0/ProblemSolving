def solution(board, skill):
    N, M = len(board), len(board[0])

    # skills 처리 배열
    temp = [[0] * (M + 1) for _ in range(N + 1)]
    for one_skill in skill:
        type, r1, c1, r2, c2, degree = one_skill

        if type == 1:
            degree = -degree

        temp[r1][c1] += degree
        temp[r1][c2 + 1] -= degree
        temp[r2 + 1][c1] -= degree
        temp[r2 + 1][c2 + 1] += degree

    # prefix sum 연산
    # 1) 열마다 가로기준 prefix sum 연산
    for i in range(N):
        for j in range(M):
            temp[i][j + 1] += temp[i][j]
    # 2) 행마다 세로기준 prefix sum 연산
    for j in range(M):
        for i in range(N):
            temp[i + 1][j] += temp[i][j]

    # 기존 배열에 연산 적용
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += temp[i][j]
            if board[i][j] >= 1:
                answer += 1
    return answer
