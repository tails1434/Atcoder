N, x = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)

for i in range(1,N):
    if a[i-1] + a[i] > x:
        if a[i] > (a[i] + a[i-1]) - x:
            a[i] -= (a[i] + a[i-1]) - x
            continue
        else:
            a[i] = 0
            a[i-1] = x
            continue

print(sum_a - sum(a))