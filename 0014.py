def applyCollatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def genCollatz(n, len):
    if n == 1:
        return len
    else:
        final_len = genCollatz(applyCollatz(n), len+1)
        return final_len

len = 0
max_len = 0
max_num = 0

for i in range (1, 1000001):
    len = genCollatz(i, 1)
    if len > max_len:
        max_len = len
        max_num = i

print(max_num)