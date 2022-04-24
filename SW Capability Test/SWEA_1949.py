def init():
    grid_size, depth = tuple(map(int, input().split()))
    grid = [ list(map(int, input().split())) for _ in range(grid_size) ]
    visited = [[False] * grid_size for _ in range(grid_size)]

    return grid_size, depth, grid, visited


def get_max_value():
    result = 1
    for y in range(grid_size):
        for x in range(grid_size):
            result = max(grid[y][x], result)
    return result


def get_start_pos():
    global max_value
    result = []

    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] == max_value:
                result.append((y, x))
    return result


def in_range(y, x):
    return 0 <= y < grid_size and 0 <= x < grid_size


def can_go(y, x, height):
    return in_range(y, x) and grid[y][x] < height


def dfs(current_pos, count, is_cut):
    # 2. 만약 자기보다 높이가 높거나 같은 봉우리를 만났을 경우, 아직 등산로를 한번도 변경한 적이 없다면 해당 지형을 깎는다.
    global visited, answer
    if answer < count:
        answer = count

    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    y, x = current_pos

    for dy, dx in zip(dys, dxs):
        next_y, next_x = y + dy, x + dx
        next_pos = (next_y, next_x)

        if in_range(next_y, next_x) and not visited[next_y][next_x]:
            # 내리막길인 경우
            if grid[y][x] > grid[next_y][next_x]:
                visited[next_y][next_x] = True
                dfs(next_pos, count + 1, is_cut)
                visited[next_y][next_x] = False

            # 내리막길이 아닌 경우 및 아직 공사를 안 했다면,
            elif grid[y][x] <= grid[next_y][next_x] and not is_cut:
                for current_depth in range(1, depth + 1):
                    # 공사하기
                    is_cut = True
                    grid[next_y][next_x] -= current_depth

                    if grid[y][x] > grid[next_y][next_x]:
                        visited[next_y][next_x] = True
                        dfs(next_pos, count + 1, is_cut)
                        visited[next_y][next_x] = False

                    # 공사 취소하기 (다른 경우를 체크해주기 위해)
                    is_cut = False
                    grid[next_y][next_x] += current_depth


def solve():
    global start_pos, visited

    # 1. 시작 봉우리가 최대 5개이므로 이 지점부터 모든 경우를 탐색한다.
    for one_start_pos in start_pos:
        visited = [ [False] * grid_size for _ in range(grid_size) ]
        y, x = one_start_pos
        visited[y][x] = True
        dfs(one_start_pos, 1, False)


for test_case in range(1, int(input()) + 1):
    grid_size, depth, grid, visited = init()
    visited = [ [False] * grid_size for _ in range(grid_size) ]
    max_value = get_max_value()
    start_pos = get_start_pos()

    answer = 0
    solve()
    print(f'#{test_case} {answer}')


'''
1
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''
'''
10
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2
1 2 1
2 1 2
1 2 1
5 2
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
4 1
6 6 1 7
3 6 6 1
2 4 2 4
7 1 3 4
5 5
18 18 1 8 18
17 7 2 7 2
17 8 7 4 3
17 9 6 5 16
18 10 17 13 18
6 4
12 3 12 10 2 2
13 7 13 3 11 6
2 2 6 5 13 9
1 12 5 4 10 5
11 10 12 8 2 6
13 13 7 4 11 7
7 3
16 10 14 14 15 14 14
15 7 12 2 6 4 9
10 4 11 4 6 1 1
16 4 1 1 13 9 14
3 12 16 14 8 13 9
3 4 17 15 12 15 1
6 6 13 6 6 17 12
8 5
2 3 4 5 4 3 2 1
3 4 5 6 5 4 3 2
4 5 6 7 6 5 4 3
5 6 7 8 7 6 5 4
6 7 8 9 8 7 6 5
5 6 7 8 7 6 5 4
4 5 6 7 6 5 4 3
3 4 5 6 5 4 3 2
8 2
5 20 15 11 1 17 10 14
1 1 11 16 1 14 7 5
17 2 3 4 5 13 19 20
6 18 5 16 6 7 8 5
10 4 5 4 9 2 10 16
2 7 16 5 8 9 10 11
12 19 18 8 7 11 15 12
1 20 18 17 16 15 14 13
'''
