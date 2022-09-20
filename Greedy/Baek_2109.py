n = int(input())
universities = list()

for _ in range(n):
    universities.append(tuple(map(int, input().split())))

universities.sort(key=lambda x: -x[0])

answer = 0
schedule = dict()

for university in universities:
    p, d = university
    for day in range(d, 0, -1):
        if day not in schedule:
            schedule[day] = 1
            answer += p
            break

print(answer)

'''
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
'''
