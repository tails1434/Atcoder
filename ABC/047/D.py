N, T = map(int, input().split())
A = list(map(int, input().split()))

max_bef = 0
cnt = 0
A_min = A[0]

for i in range(1,N):
    tmp = A[i] - A_min
    if max_bef < tmp:
        max_bef = tmp
        cnt = 0
    if max_bef == tmp:
        cnt += 1
    A_min = min(A_min, A[i])

print(cnt)
