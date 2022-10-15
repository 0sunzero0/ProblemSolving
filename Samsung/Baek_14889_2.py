N = int(input())
grid = [ list(map(int, input().split())) for _ in range(N) ]

members = [ member for member in range(1, N + 1) ]
team1 = []
team2 = []
min_diff = 1000


def get_diff(a, b):
    team1_capability = 0
    team2_capability = 0

    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                team1_capability += grid[a[i]-1][a[j]-1]
                team2_capability += grid[b[i]-1][b[j]-1]

    return abs(team1_capability - team2_capability)


def choose(idx):
    global min_diff, team1, team2
    if idx == len(members):
        if len(team1) == N//2:
            team2 = [member for member in members if member not in team1]
            min_diff = min(min_diff, get_diff(team1, team2))
        return

    team1.append(members[idx])
    choose(idx + 1)
    team1.pop()
    choose(idx + 1)


choose(0)
print(min_diff)
'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
