from collections import deque


def init():
    N, K = int(input()), int(input())
    apple = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(K):
        y, x = tuple(map(int, input().split()))
        apple[y][x] = True

    L = int(input())
    snake_moves = list()
    for _ in range(L):
        snake_moves.append(input().split())

    times = dict()
    for snake_move in snake_moves:
        time, direct = snake_move
        time = int(time)
        times[time] = direct

    return N, K, apple, L, snake_moves, times


def change_direct(option):
    global current_dir_idx

    # 왼쪽으로 90도 회전
    if option == 'L':
        current_dir_idx = (current_dir_idx - 1) % 4
    # 오른쪽으로 90도 회전
    else:
        current_dir_idx = (current_dir_idx + 1) % 4


def in_range(y, x):
    return 1 <= y <= N and 1 <= x <= N


def is_twisted(pos, queue):
    return pos in queue


def move():
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    y, x = snake[0]
    ny, nx = dys[current_dir_idx] + y, dxs[current_dir_idx] + x

    # 범위에 벗어나면
    if not in_range(ny, nx):
        return False

    # 머리 내밀기
    if is_twisted((ny, nx), snake):
        return False
    snake.appendleft((ny, nx))

    # 사과가 없다면 꼬리 빼기
    if not apple[ny][nx]:
        snake.pop()
    # 사과가 있다면 사과 없애기
    else:
        apple[ny][nx] = False

    return True


def simulate():
    global answer

    while True:
        if answer in times:
            change_direct(times[answer])

        answer += 1
        if not move():
            return


N, K, apple, L, snake_moves, times = init()
current_dir_idx = 1
snake = deque()
snake.append((1, 1))
answer = 0
simulate()
print(answer)

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
'''
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
'''
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''
