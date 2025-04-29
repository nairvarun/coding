n = int(input())

res = 0
i = 5
while n // i > 0:
    res += n // i
    i *= 5
print(res)
