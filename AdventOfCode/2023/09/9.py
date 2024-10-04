'''
# 1
with open('9.txt') as f:
    prediction = 0
    for line in f.readlines():
        line = list(map(int, line.split()))
        last = [line[-1]]
        while not all(i == 0 for i in line):
            line = [line[next_idx] - num for next_idx, num in enumerate(line[:-1], start=1)]
            last.append(line[-1])
        p = 0
        for i in last[::-1]:
            p += i
        prediction += p
print(prediction)
'''

# 2
with open('9.txt') as f:
    prediction = 0
    for line in f.readlines():
        line = list(map(int, line.split()))
        first = [line[0]]
        while not all(i == 0 for i in line):
            line = [line[next_idx] - num for next_idx, num in enumerate(line[:-1], start=1)]
            first.append(line[0])
        p = 0
        for i in first[::-1]:
            p = i - p
        prediction += p
print(prediction)
