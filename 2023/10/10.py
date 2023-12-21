'''
# 1
pipes = open('10.txt').read().splitlines()
Y, X = len(pipes)-1, len(pipes[0])-1
y, x = [(pipes.index(tiles), tiles.index('S')) for tiles in pipes if 'S' in tiles][0]

arr = []
if y != 0 and pipes[y-1][x] in '|7F':
    arr.append((y-1, x))
    facing = 'n'
if y != Y and pipes[y+1][x] in '|JL':
    arr.append((y+1, x))
    facing = 's'
if x != X and pipes[y][x+1] in '-7J':
    arr.append((y, x+1))
    facing = 'e'
if x != 0 and pipes[y][x-1] in '-Fl':
    arr.append((y, x-1))
    facing = 'w'

end, curr = arr
print(end, curr, facing)
print()
tiles = 2
while curr != end:
    print(curr, facing)
    y, x = curr
    match pipes[y][x]:
        case '|':
            y += 1 if facing == 's' else -1
        case '-':
            x += 1 if facing == 'e' else -1
        case 'L':
            if facing == 's':
                x += 1
                facing = 'e'
            else:
                y -= 1
                facing = 'n'
        case 'J':
            if facing == 's':
                x -= 1
                facing = 'w'
            else:
                y -= 1
                facing = 'n'
        case '7':
            if facing == 'n':
                x -= 1
                facing = 'w'
            else:
                y += 1
                facing = 's'
        case 'F':
            if facing == 'n':
                x += 1
                facing = 'e'
            else:
                y += 1
                facing = 's'
    curr = (y, x)
    tiles += 1
print(tiles//2)
'''

# 2
from collections import deque

grid = open('10.txt').read().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            sr, sc = r, c
            break
    else:
        continue
    break

s = {'|', '-', 'J', 'L', '7', 'F'}
loop = {(sr, sc)}
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]

    if r > 0 and ch in 'S|JL' and grid[r-1][c] in '|7F' and (r-1, c) not in loop:
        loop.add((r-1, c))
        q.append((r-1, c))
        if ch == 'S':
            s &= {'|', 'J', 'L'}

    if r < len(grid) and ch in 'S|7F' and grid[r+1][c] in '|JL' and (r+1, c) not in loop:
        loop.add((r+1, c))
        q.append((r+1, c))
        if ch == 'S':
            s &= {'|', '7', 'F'}

    if c > 0 and ch in 'S-J7' and grid[r][c-1] in '-LF' and (r, c-1) not in loop:
        loop.add((r, c-1))
        q.append((r, c-1))
        if ch == 'S':
            s &= {'-', 'J', '7'}

    if c < len(grid[r]) and ch in 'S-LF' and grid[r][c+1] in '-J7' and (r, c+1) not in loop:
        loop.add((r, c+1))
        q.append((r, c+1))
        if ch == 'S':
            s &= {'-', 'L', 'F'}


assert len(s) == 1
(S,) = s
grid = [row.replace('S', S) for row in grid]
grid = [''.join(ch if (r, c) in loop else '.' for c, ch in enumerate(row))for r, row in enumerate(grid)]

outside = set()
for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == '|':
            assert up is None
            within = not within
        elif ch == '-':
            assert up is not None
        elif ch in 'LF':
            assert up is None
            up = ch == 'L'
        elif ch in '7J':
            assert up is not None
            if ch != ('J' if up else '7'):
                within = not within
            up = None
        elif ch == '.':
            pass
        else:
            raise RuntimeError(f'unexpected character: {ch}')

        if not within:
            outside.add((r, c))

print(len(grid) * len(grid[0]) - len(outside | loop))
