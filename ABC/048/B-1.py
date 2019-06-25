a, b, x = map(int, input().split())

b_div = b // x
a_div = a // x + (-1 if a % x == 0 else 0)

print(b_div - a_div)