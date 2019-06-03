N = int(input())
t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)

for i in range(1,N+1):
    t[i],x[i],y[i] = map(int, input().split())
    a = t[i] - t[i-1]
    b = abs(x[i] - x[i-1])
    c = abs(y[i] - y[i-1])
    if a % 2 == 0:
        if b + c <= a and (b + c) % 2 == 0:
            continue
        else:
            print('No')
            exit()
    else:
        if b + c <= a and (b + c) % 2 == 1:
            continue
        else:
            print('No')
            exit()

print('Yes')