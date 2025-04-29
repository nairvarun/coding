print(n := int(input()), end=' ')
while n != 1:
    print(n := n//2, end=' ') if n & 1 == 0 else print(n := n*3+1, end=' ')
