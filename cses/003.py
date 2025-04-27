res = 0
cnt = 0
prev = ''
for i in input():
    if i != prev:
        res = max(cnt, res)
        prev = i
        cnt = 1
        continue
    cnt += 1
print(max(res, cnt))
