def sq_sum(n):
    s = 0
    for i in range(n + 1):
        s += i**2
    return s

def sum_sq(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s**2

print(sum_sq(100) - sq_sum(100))