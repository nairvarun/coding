for i in range(int(input())):
    r, c = map(int, input().split())
    mx = max(r, c)
    hi = mx ** 2
    lo = (mx-1) ** 2 + 1
    t2l = mx % 2 == 0
    if c < r:
        if t2l:
            print(hi - c + 1)
        else:
            print(lo + c - 1)
    else:
        if t2l:
            print(lo + r - 1)
        else:
            print(hi - r + 1)
