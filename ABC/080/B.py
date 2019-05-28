N = int(input())

n = N
sum_X = 0
while N > 0:
    sum_X += N % 10
    N = N // 10

if n % sum_X == 0:
    print('Yes')
else:
    print('No')