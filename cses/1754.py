for _ in range(int(input())):
    x, y = map(int, input().split())

    if min(x, y) == 0 and x + y > 0:
        print('NO')
        continue
    
    if x + y == 3:
        print('YES')
        continue
    
    if (x + y) % 3 != 0:
        print('NO')
        continue

    if min(x, y) * 2 < max(x, y):
        print('NO')
        continue

    print('YES')
    
