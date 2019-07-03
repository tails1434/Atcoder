N, M = map(int, input().split())

cnt = 0
if N > M // 2:
    cnt = M // 2
else:
    cnt = N + ((M - 2 * N) // 4)

print(cnt)