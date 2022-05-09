def recursive(current_picked):
    global answer

    if len(current_picked) == N:
        sum = 0
        for i in range(N - 1):
            sum += abs(current_picked[i] - current_picked[i + 1])
        answer = max(answer, sum)

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            current_picked.append(A[i])

            recursive(current_picked)

            visited[i] = 0
            current_picked.pop()


N = int(input())
A = list(map(int, input().split()))
visited = [0] * N

answer = 0
recursive([])
print(answer)

'''
6
20 1 15 8 4 10
'''
