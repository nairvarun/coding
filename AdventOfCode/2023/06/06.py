'''
# 1
with open('6.txt') as f:
    time, dist = (list(map(int, x.split(':')[1].strip().split())) for x in f.readlines())

res = 1
for idx, i in enumerate(time):
    count = 0
    for j in range((i//2)+1):
        if j * (i-j) > dist[idx]:
            count += 2
    if i % 2 == 0:
        res *= count - 1
    else:
        res *= count

print(res)
'''

# 2
with open('6.txt') as f:
    time, dist = (int(x.split(':')[1].strip().replace(' ', '')) for x in f.readlines())

for t in range((time//2)+1):
    if t * (time-t) > dist:
        print(time - (2*t) + 1)
        break
