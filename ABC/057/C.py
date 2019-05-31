import math
N = int(input())

sqrt_N = int(math.sqrt(N))
min_F = float('inf')

for i in range(1,sqrt_N + 1):
    if N % i == 0:
        A = i
        B = N // i
        if min_F > max(len(str(A)),len(str(B))):
            min_F = max(len(str(A)),len(str(B)))

print(min_F)