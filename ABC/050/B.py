N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [0] * M
X = [0] * M
for i in range(M):
    cnt = 0
    P, X = map(int, input().split())
    for j in range(N):
        if j == P-1:
            cnt += X
        else:
            cnt += T[j]
    print(cnt)