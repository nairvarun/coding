from itertools import combinations

# # 1
# space = open('11.txt').read().strip().splitlines()

# # find empty rows and empty cols
# er, ec = {i for i in range(len(space))}, {i for i in range(len(space[0]))}
# for r, row in enumerate(space):
#     seen_galaxy = False
#     for c, ch in enumerate(row):
#         if ch == '#':
#             seen_galaxy = True
#             if c in ec:
#                 ec.remove(c)
#     if seen_galaxy:
#         if r in er:
#             er.remove(r)

# # expand emty cols
# space = [''.join(['..' if idx in ec else i for idx, i in enumerate(row)]) for row in space]
# # expand empty rows
# empty_space = '.'*len(space[0])
# for offset, r in enumerate(er):
#     space.insert(r+offset, empty_space)

# # find galaxies
# galaxies = [(r, c) for r, row in enumerate(space) for c, ch in enumerate(row) if ch == '#']
# pairs = combinations(galaxies, 2)

# res = 0
# for (r1, c1), (r2, c2) in pairs:
#     res += abs(r2 - r1) + abs(c2 - c1)
# print(res)


# 2
space = open('11.txt').read().strip().splitlines()

# find empty rows and empty cols
er = {r for r, row in enumerate(space) if all(ch == '.' for ch in row)}
ec = {c for c, col in enumerate(zip(*space)) if all(ch == '.' for ch in col)}

# calc offset coords
points = {(r, c): (r, c) for r, row in enumerate(space) for c, ch in enumerate(row)}
MIL = 999999
r_offset = 0
for r, row in enumerate(space):
    if r in er:
        r_offset += MIL
    c_offset = 0
    for c, ch in enumerate(row):
        if c in ec:
            c_offset += MIL
        points[(r, c)] = (r+r_offset, c+c_offset)

# find galaxies
galaxies = [points[(r, c)] for r, row in enumerate(space) for c, ch in enumerate(row) if ch == '#']
pairs = combinations(galaxies, 2)
res = 0
i = 0
for (r1, c1), (r2, c2) in pairs:
    res += abs(r2 - r1) + abs(c2 - c1)
print(res)


# # 2 (cleaner but slower)
# space = open('11.txt').read().splitlines()

# empty_rows = [r for r, row in enumerate(space) if all(ch == '.' for ch in row)]
# empty_cols = [c for c, col in enumerate(zip(*space)) if all(ch == '.' for ch in col)]
# pairs = combinations([(r, c) for r, row in enumerate(space) for c, ch in enumerate(row) if ch == '#'], 2)

# res = 0
# offset = 1000000
# for (r1, c1), (r2, c2) in pairs:
#     for r in range(min(r1, r2), max(r1, r2)):
#         res += offset if r in empty_rows else 1
#     for c in range(min(c1, c2), max(c1, c2)):
#         res += offset if c in empty_cols else 1
# print(res)
