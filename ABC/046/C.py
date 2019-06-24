N = int(input())

T = [0] * N
A = [0] * N
for i in range(N):
    A[i], T[i] = map(int, input().split())

tmp_T = T[0]
tmp_A = A[0]

for i in range(1,N):
    ma = tmp_A // A[i] + (1 if tmp_A % A[i] > 0 else 0)
    mt = tmp_T // T[i] + (1 if tmp_T % T[i] > 0 else 0)
    n = max(mt,ma)
    tmp_A = n * A[i]
    tmp_T = n * T[i]

print(tmp_T + tmp_A)