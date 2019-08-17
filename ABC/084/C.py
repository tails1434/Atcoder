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
    
    # j → j + 1区間の最短時間を求めていく
    for j in range(i, N-1):
        # 駅j+1を出発する時刻は S[j] + F[j] * k となる
        # これがt以上になる最小のkを求める
        k_tmp = math.ceil((t - S[j])/F[j])
        k = max(0,k_tmp)

        t = S[j] + F[j] * k + C[j]
    
    print(t)


