# # 1
# def count(cfg, nums):
#     if cfg == '':
#         return 1 if nums == () else 0

#     if nums == ():
#         return 0 if '#' in cfg else 1

#     res = 0
#     if cfg[0] in '.?':
#         res += count(cfg[1:], nums)

#     if cfg[0] in '#?':
#         if len(cfg) >= nums[0] and '.' not in cfg[:nums[0]] and (len(cfg) == nums[0] or cfg[nums[0]] != '#'):
#             res += count(cfg[nums[0]+1:], nums[1:])

#     return res

# res = 0
# with open('12.txt') as f:
#     for line in f.readlines():
#         cfg, nums = line.split()
#         nums = tuple(map(int, nums.split(',')))
#         res += count(cfg, nums)
# print(res)

# 2
cache = {}
def count(cfg, nums):
    if cfg == '':
        return 1 if nums == () else 0

    if nums == ():
        return 0 if '#' in cfg else 1

    key = (cfg, nums)
    if key in cache:
        return cache[key]

    res = 0
    if cfg[0] in '.?':
        res += count(cfg[1:], nums)

    if cfg[0] in '#?':
        if len(cfg) >= nums[0] and '.' not in cfg[:nums[0]] and (len(cfg) == nums[0] or cfg[nums[0]] != '#'):
            res += count(cfg[nums[0]+1:], nums[1:])

    cache[key] = res
    return res

res = 0
with open('12.txt') as f:
    for line in f.readlines():
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        cfg = '?'.join([cfg]*5)
        nums *= 5
        # print(cfg, nums)
        res += count(cfg, nums)
print(res)
