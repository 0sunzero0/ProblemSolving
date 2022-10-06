from collections import defaultdict, deque
import sys
sys.setrecursionlimit(2 ** 10)


def make_graph():
    for section in range(1, N + 1):
        info = list(map(int, input().split()))
        del info[0]
        for end in info:
            graph[section].append(end)
            graph[end].append(section)


def initialize_bfs_visit():
    global bfs_visit
    bfs_visit = set()


def can_go(section, group):
    return section not in bfs_visit and section in group


def bfs(start, group):
    bfs_queue = deque([start])
    bfs_visit.add(start)
    total = populations[start]

    while bfs_queue:
        cur_section = bfs_queue.popleft()
        for next_section in graph[cur_section]:
            if can_go(next_section, group):
                bfs_queue.append(next_section)
                bfs_visit.add(next_section)
                total += populations[next_section]

    if len(group) == len(bfs_visit):
        return True, total
    return False, 0


def get_all_combination(section):
    global answer
    if section == N + 1:
        set_a = set()
        set_b = set()
        for section in range(1, N + 1):
            if comb_visit[section]:
                element_a = section
                set_a.add(section)
            else:
                element_b = section
                set_b.add(section)

        if len(set_a) == 0 or len(set_b) == 0:
            return

        initialize_bfs_visit()
        is_connected_a, sum_a = bfs(element_a, set_a)
        initialize_bfs_visit()
        is_connected_b, sum_b = bfs(element_b, set_b)

        if is_connected_a and is_connected_b:
            answer = min(answer, abs(sum_a - sum_b))
        return

    comb_visit[section] = True
    get_all_combination(section + 1)
    comb_visit[section] = False
    get_all_combination(section + 1)


def print_answer():
    if answer == MAX_VALUE:
        print(-1)
    else:
        print(answer)


MAX_VALUE = 1000 * 10 * 100
N = int(input())
populations = [0] + list(map(int, input().split()))

graph = defaultdict(list)
comb_visit = [[False] * (N + 1) for _ in range(N + 1)]
bfs_visit = set()


answer = MAX_VALUE
make_graph()
get_all_combination(1)
print_answer()

'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''
'''
6
1 1 1 1 1 1
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''
