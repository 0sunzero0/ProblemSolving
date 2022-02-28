N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def go(index, sum):
    global count
    if index == N :
        if sum == S:    count += 1
        return

    go(index + 1, sum + arr[index])
    go(index + 1, sum)

go(0, 0)
if S == 0:
    count -= 1
print(count)
