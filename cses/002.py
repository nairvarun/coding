n = int(input())
total = sum(map(int, input().split()))
expected_total = n*(n+1)//2
print(expected_total - total)

