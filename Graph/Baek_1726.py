from collections import deque

import sys
input = sys.stdin.readline

# 동 서 남 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

rotate_all_dir = ((2, 3), (2, 3), (0, 1), (0, 1))


def in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def is_orbit(r, c):
    return grid[r][c] == 0


def bfs():
    visit = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    visit[start_r][start_c][start_d] = True
    bfs_queue = deque([(start_r, start_c, start_d, 0)])

    while bfs_queue:
        cur_r, cur_c, cur_d, count = bfs_queue.popleft()
        # 목표 위치와 방향에 도착하면 count 리턴
        if (cur_r, cur_c, cur_d) == (end_r, end_c, end_d):
            return count

        # 1, 2, 3칸 직진
        for step in range(1, 4):
            next_r = cur_r + dr[cur_d] * step
            next_c = cur_c + dc[cur_d] * step
            next_d = cur_d

            if not in_range(next_r, next_c) or not is_orbit(next_r, next_c):
                break
            if not visit[next_r][next_c][next_d]:
                bfs_queue.append((next_r, next_c, next_d, count + 1))
                visit[next_r][next_c][next_d] = True

        # 방향 바꾸기 - 왼쪽 90도, 오른쪽 90도
        for next_d in rotate_all_dir[cur_d]:
            if not visit[cur_r][cur_c][next_d]:
                bfs_queue.append((cur_r, cur_c, next_d, count + 1))
                visit[cur_r][cur_c][next_d] = True


N, M = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
start_r, start_c, start_d = tuple(map(int, input().split()))
end_r, end_c, end_d = tuple(map(int, input().split()))

start_r -= 1
start_c -= 1
start_d -= 1

end_r -= 1
end_c -= 1
end_d -= 1

print(bfs())

'''
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 1
'''
