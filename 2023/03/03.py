'''
# 3
f = open('3.txt')

lines = f.readlines()
row, col = 0, 0
last_col = len(lines[0])-1
res = 0
while row < len(lines):
    col = 0
    while col < last_col:
        if lines[row][col].isdigit():
            start = col
            while lines[row][col].isdigit() and col < last_col:
                col += 1
            if row == 0:
                if not all([ch == '.' for x in (lines[row+1][max(0, start-1):min(last_col, col+1)], lines[row][start-1] if start != 0 else '.', lines[row][col] if col != last_col else '.') for ch in x]):
                    res += int(lines[row][start:col])
            elif row == len(lines)-1:
                if not all([ch == '.' for x in (lines[row-1][max(0, start-1):min(last_col, col+1)], lines[row][start-1] if start != 0 else '.', lines[row][col] if col != last_col else '.') for ch in x]):
                    res += int(lines[row][start:col])
            else:
                if not all(ch == '.' for x in (lines[row-1][max(0, start-1):min(last_col, col+1)], lines[row+1][max(0, start-1):min(last_col, col+1)], lines[row][start-1] if start != 0 else '.', lines[row][col] if col != last_col else '.') for ch in x):
                    res += int(lines[row][start:col])
        else:
            col += 1
    row += 1
print(res)

f.close()
'''

# 2
f = open('3.txt')
# f = open('a.txt')

lines = f.readlines()
row, col = 0, 0
last_col = len(lines[0])-1
res = 0
maybe_gears = {}

while row < len(lines):
    col = 0
    while col < last_col:
        if lines[row][col].isdigit():
            start = col
            while lines[row][col].isdigit() and col < last_col:
                col += 1
            num = int(lines[row][start:col])

            if start != 0 and lines[row][start-1] == '*':
                key = f"{row}-{start-1}"
                maybe_gears[key] = maybe_gears.get(key, []) + [num]
            if col != last_col and lines[row][col] == '*':
                key = f"{row}-{col}"
                maybe_gears[key] = maybe_gears.get(key, []) + [num]
            if row != 0 and '*' in lines[row-1][max(0, start-1):min(last_col, col+1)]:
                key = f"{row-1}-{lines[row-1][max(0, start-1):min(last_col, col+1)].index('*') + max(0, start-1)}"
                maybe_gears[key] = maybe_gears.get(key, []) + [num]
            if row != len(lines)-1 and '*' in lines[row+1][max(0, start-1):min(last_col, col+1)]:
                key = f"{row+1}-{lines[row+1][max(0, start-1):min(last_col, col+1)].index('*') + max(0, start-1)}"
                maybe_gears[key] = maybe_gears.get(key, []) + [num]
        else:
            col += 1
    row += 1

for k, v in maybe_gears.items():
    if len(v) == 2:
        res += v[0]*v[1]

print(res)

f.close()
