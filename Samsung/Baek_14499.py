import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

dy = [0, 1, -1, 0, 0]
dx = [0, 0, 0, -1, 1]

dice = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

while command:
        direction = command.pop(0)
        nx, ny = x + dx[direction], y + dy[direction]
        temp01, temp10, temp11, temp12, temp21, temp31  = dice[0][1], dice[1][0], dice[1][1], dice[1][2], dice[2][1], dice[3][1]

        if 0 <= nx < N and 0 <= ny < M:
                if direction == 1:
                        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = temp31, temp10, temp11, temp12
                elif direction == 2:
                        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = temp11, temp12, temp31, temp10
                elif direction == 3:
                        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = temp11, temp21, temp31, temp01
                elif direction == 4:
                        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = temp31, temp01, temp11, temp21
                    
                x, y = nx, ny
                if graph[x][y] == 0:
                        graph[x][y] = dice[3][1]
                else:
                        dice[3][1] = graph[x][y]
                        graph[x][y] = 0

                print(dice[1][1])

'''
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
'''
