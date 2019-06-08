import math

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i],y[i] = map(int, input().split())

ans = 0

for i in range(N):
    for j in range(N):
        length = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 )
        if ans < length:
            ans = length

print(ans)