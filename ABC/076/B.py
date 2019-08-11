N = int(input())
K = int(input())

ans = float('inf')

for i in range(N+1):
    digit = 1
    tmp = digit * 2 ** i + (N - i) * K
    if ans > tmp:
        ans = tmp

print(ans)