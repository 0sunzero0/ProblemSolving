def make_one(N, count):
    if N == 1:
        global ret
        ret = min(ret, count)
        return

    if N % 2 == 0: make_one(N / 2, count + 1)
    if N % 3 == 0: make_one(N / 3, count + 1)
    make_one(N - 1, count + 1)


N = int(input())
ret = 1000000
make_one(N, 0)
print(ret)
