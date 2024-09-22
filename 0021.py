from math import ceil 
from functools import reduce

d = lambda n: sum(i for i in range(1, ceil(n/2) + 1) if n % i == 0)

is_amicable = lambda n: True if d(d(n)) == n and n != d(n) else False

add = lambda a, b: a + b

amicable_sum = reduce(add, filter(is_amicable, (i for i in range(10000))))

print(amicable_sum)

