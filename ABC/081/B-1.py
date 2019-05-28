N = int(input())
A = list(map(int, input().split()))

res = float('inf')

for i in range(N):
    count = 0

    while A[i] % 2 == 0:
        A[i] /= 2
        count += 1

    if res > count:
        res = count

print(res)