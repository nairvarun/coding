# part 1
res = 0
with open('input.txt') as f:
    for line in f.readlines():
        l = list(map(int, line.split()))
        if l[0] < l[1]:
            for idx, i in enumerate(l[:-1]):
                d = l[idx+1] - i
                if not 1 <= d <= 3:
                    break
            else:
                res += 1
            continue
        elif l[0] > l[1]:
            for idx, i in enumerate(l[:-1]):
                d = i - l[idx+1]
                if not 1 <= d <= 3:
                    break
            else:
                res += 1
            continue
print(res)

# part 2
def pos(n):
    return n > 0

res = 0
with open('test.txt') as f:
    for line in f.readlines():
        l = list(map(int, line.split()))
        flag = False
        for idx, i in enumerate(l):
            if flag:
                break

print(res)

