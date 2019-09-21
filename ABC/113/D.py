def main():
    H, W, K = map(int, input().split())
    
    if W == 1:
        print(1)
        exit()

    MOD = 10 ** 9 + 7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1

    for h in range(H):
        # 1: 線あり、 0: 線なし
        for i in range(2 ** (W-1)):
            # 連続した1がある→隣接する列に線が引かれている
            if bin(i).count('11') >= 1:
                continue
            perm = [k for k in range(W)]
            for j in range(W-1):
                if (i >> j) & 1:
                    perm[j], perm[j+1] = perm[j+1], perm[j]

            for j in range(W):
                dp[h+1][perm[j]] += dp[h][j]
                dp[h+1][perm[j]] %= MOD

    print(dp[H][K-1])



main()