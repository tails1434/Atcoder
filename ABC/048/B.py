a, b, x = map(int, input().split())

if a % x == 0:
    ans = (b // x) - (a // x) + 1
else:
    ans = (b // x) - (a // x)

print(ans)