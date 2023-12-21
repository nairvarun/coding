# # 1
# def find_mirror(pattern):
#     for r in range(1, len(pattern)):
#         above = pattern[:r][::-1]
#         below = pattern[r:]

#         above = above[:len(below)]
#         below = below[:len(above)]

#         if above == below:
#             return r
#     return 0

# res = 0
# for pattern in open('13.txt').read().split('\n\n'):
#     pattern = pattern.splitlines()
#     row = find_mirror(pattern)
#     col = find_mirror(list(zip(*pattern)))
#     res += (row * 100) + col
# print(res)

# 2
def find_mirror(pattern):
    for r in range(1, len(pattern)):
        above = pattern[:r][::-1]
        below = pattern[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r
    return 0

res = 0
for pattern in open('13.txt').read().split('\n\n'):
    pattern = pattern.splitlines()
    row = find_mirror(pattern)
    col = find_mirror(list(zip(*pattern)))
    res += (row * 100) + col
print(res)
