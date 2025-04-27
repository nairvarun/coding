_ = input()
nums = map(int, input().split())
res = 0

prev = 0
for i in nums:
    if i < prev:
        res += prev - i
    prev = max(prev, i)

print(res)
