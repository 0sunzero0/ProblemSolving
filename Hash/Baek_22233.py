N, M = tuple(map(int, input().split()))
keyword_dict = dict()
blog_list = list()

for _ in range(N):
    keyword = input()
    keyword_dict[keyword] = ''
for _ in range(M):
    writing = input()
    blog_list.append(writing)

for writing in blog_list:
    for keyword in writing.split(","):
        if keyword in keyword_dict:
            del keyword_dict[keyword]
    print(len(keyword_dict))

'''
5 2
map
set
dijkstra
floyd
os
map,dijkstra
map,floyd
'''
