from heapq import *
from collections import Counter

# part 1
l, r = [], []
with open('input.txt') as f:
    for line in f.readlines():
        a, b = map(int, line.split())
        heappush(l, a)
        heappush(r, b)

res = 0
while l:
    res += abs(heappop(l) - heappop(r))
print(res)

# part 2
l, r = [], []
with open('input.txt') as f:
    for line in f.readlines():
        a, b = map(int, line.split())
        l.append(a)
        r.append(b)
cnt = Counter(r)
res = 0
for i in l:
    res += i * cnt[i]
print(res)
