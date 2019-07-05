import math
N = int(input())
N_sqrt = math.floor(math.sqrt(N))

ans = float('inf')
for i in range(1, N_sqrt + 1):
    if N % i == 0:
        if ans > max(len(str(i)), len(str(N // i))):
            ans = max(len(str(i)), len(str(N // i)))

print(ans)