N, M = tuple(map(int, input().split()))
keyword_set = set()
blog_list = list()

for _ in range(N):
    keyword = input()
    keyword_set.add(keyword)
for _ in range(M):
    writing = input()
    blog_list.append(writing)

for writing in blog_list:
    writing_keyword_set = set(writing.split(","))
    keyword_set -= writing_keyword_set
    print(len(keyword_set))

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
