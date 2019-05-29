W, H, N = map(int, input().split())

x1 = 0
x2 = W
y1 = 0
y2 = H

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        if x1 < x:
            x1 = x
    elif a == 2:
        if x2 > x:
            x2 = x
    elif a == 3:
        if y1 < y:
            y1 = y
    elif a == 4:
        if y2 > y:
            y2 = y

if x1 > x2 or y1 > y2:
    print(0)
else:
    print((x2 - x1) * (y2 - y1))