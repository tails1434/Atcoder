W, a, b = map(int, input().split())

if a <= b <= a + W or a <= b + W <= a + W:
    print(0)
elif b + W < a:
    print(a - b - W)
elif b > a + W:
    print(b - a - W)