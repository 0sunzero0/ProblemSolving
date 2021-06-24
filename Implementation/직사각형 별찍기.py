'''
느낀점
1) 나누어 입력받기
a, b = map(int, input().strip().split(' '))
2) 속도 UP
from sys import stdin, stdout
input = stdin.readline 
print = stdout.write
'''

a, b = map(int, input().strip().split(' '))
for i in range(0, b):
    print("*" * a)
