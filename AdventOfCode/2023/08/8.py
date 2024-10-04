from itertools import cycle
from math import lcm

'''
# 1
dir, _, *lines = open('8.txt').read().splitlines()
network = {line[0:3]: (line[7:10], line[12:15]) for line in lines}

curr = 'AAA'
for step, d in enumerate(cycle(dir)):
    if curr == 'ZZZ':
        print(step)
        break
    curr = network[curr][0 if d == 'L' else 1]
'''

# 2
dir, _, *lines = open('8.txt').read().splitlines()
network = {line[0:3]: (line[7:10], line[12:15]) for line in lines}
start = (i for i in network if i.endswith('A'))
dist = []

for i in start:
    for step, d in enumerate(cycle(dir)):
        if i.endswith('Z'):
            dist.append(step)
            break
        i = network[i][0 if d == 'L' else 1]

print(lcm(*dist))
