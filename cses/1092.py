n = int(input())
n_sum = n * (n + 1) // 2
n_even = ((n//2) * ((n//2) + 1)) if n % 2 == 0 else (((n-1)//2) * (((n-1)//2) + 1))
n_odd = ((n//2) ** 2) if n % 2 == 0 else (((n+1)//2) ** 2)

if n_sum % 2 != 0:
    print('NO')
    exit()

if (diff := abs(n_even - n_odd)) % 2 != 0:
    print('NO')
    exit()

e2o = set()
o2e = set()

if n % 2 == 0:
    # n_even > n_odd
    if (diff // 2) % 2 == 0:
        e2o.add(diff//2)
    else:
        e2o.add(diff//2 + 1)
        o2e.add(1)
else:
    # n_even < n_odd
    if (diff // 2) % 2 == 0:
        o2e.add(diff//2 + 1)
        o2e.add(1)
        e2o.add(2)
    else:
        o2e.add(diff//2)


o2e.discard(0)
e2o.discard(0)

h1 = [i for i in range(2, n+1, 2) if i not in e2o | o2e] + [i for i in o2e]
h2 = [i for i in range(1, n+1, 2) if i not in o2e | e2o] + [i for i in e2o]

print('YES')
print(len(h1))
print(*h1)
print(len(h2))
print(*h2)
