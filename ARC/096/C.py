A, B, C, X, Y = map(int, input().split())

min_money = float('inf')

for k in range(max(X,Y) + 1):
    i = X - k
    j = Y - k
    sum_momey = 2 * k * C
    if (i > 0):
        sum_momey += i * A
    if (j > 0):
        sum_momey += j * B
    if min_money > sum_momey:
        min_money = sum_momey

print(min_money)