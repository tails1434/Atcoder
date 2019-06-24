W, H, N = map(int, input().split())
x = [0] * N
y = [0] * N
a = [0] * N
x1 = 0
x2 = W
y3 = 0
y4 = H
for i in range(N):
    x[i], y[i], a[i] = map(int, input().split())
    if a[i] == 1:
        if x1 < x[i]:
            x1 = x[i]
    elif a[i] == 2:
        if x2 > x[i]:
            x2 = x[i]
    elif a[i] == 3:
        if y3 < y[i]:
            y3 = y[i]
    elif a[i] == 4:
        if y4 > y[i]:
            y4 = y[i]

if x2-x1 <=0 or y4-y3 <= 0:
    print(0)
else:
    print((x2-x1)*(y4-y3))
