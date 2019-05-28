import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    a = 0
    b = 0
    a = math.sqrt(pow((txa-x[i]), 2) + pow((tya-y[i]), 2))
    b = math.sqrt(pow((txb-x[i]), 2) + pow((tyb-y[i]), 2))
    if a + b <= T * V:
        print('YES')
        exit()

print('NO')