from collections import defaultdict

Q = int(input())
name_to_value = defaultdict(list)
answer = 0

for _ in range(Q):
    query = list(input().split(" "))
    num, name, value = query[0], query[1], query[2:]
    if num == '1':
        name_to_value[name] += list(map(int, value[1:]))
    else:
        name_to_value[name].sort()
        count = int(value[0])

        for _ in range(count):
            if not name_to_value[name]:
                break
            answer += name_to_value[name].pop()

print(answer)

'''
7
1 Cpp 5 10 4 2 8 4
1 Java 2 8 2
2 Cpp 2
1 Cpp 2 10 3
2 Cpp 3
2 Java 1
2 Python 10
'''
