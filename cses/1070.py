from math import ceil
n = int(input())

if n == 1:
    print('1')
    exit()

if n <= 3:
    print('NO SOLUTION')
    exit()

if n == 4:
    print('2 4 1 3')
    exit()

mid = ceil(n/2)
for i in range(1, mid + 1):
    if i == mid and n % 2 != 0:
        print(f'{i}', end=' ')
    else:
        print(f'{i} {i+mid}', end=' ')
