import math
N = int(input())
C = [0] * N
S = [0] * N
F = [0] * N

for i in range(N - 1):
    C[i], S[i], F[i] = map(int, input().split())

for i in range(N):
    t = 0
    if i == N - 1:
        print(0)
        exit()

    for j in range(i, N-1):
        if t < S[j]:
            t = math.ceil(S[j]/F[j]) * F[j] + C[j]
        elif t >= S[j]:
            t += C[j] + t % F[j]
    
    print(t)


