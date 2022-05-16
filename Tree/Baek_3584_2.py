def solve():
    n = int(input())
    par = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        par[v] = u

    check = [0] * (n + 1)
    x, y = map(int, input().split())

    while x:
        check[x] = 1
        x = par[x]

    while y and check[y] == 0:
        y = par[y]
    print(y)


T = int(input())
for _ in range(T):
    solve()
