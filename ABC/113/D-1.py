def main():
    H, W, K = map(int, input().split())

    dp = [[0] * (W + 5) for _ in range(H + 5)]

    dp[0][0] = 1
    MOD = 10**9 + 7

    for h in range(H):
        for j in range(1 << W-1):
            a = str(bin(j))[2:].zfill(W-1)
            
            #|   |   |    |   |   |    |   |   |
            #| - |   | or |   | - | or |   |   | 
            #|   |   |    |   |   |    |   |   |
            # の3通りを考えれば良い　

            if a.count('11') >= 1:
                continue
            for w in range(W):
                if w == 0:
                    # まっすぐ移動
                    if a[w] == '0':
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD
                    # 右へ移動
                    if a[w] == '1':
                        dp[h+1][w+1] += dp[h][w]
                        dp[h+1][w+1] %= MOD
                elif w == W-1:
                    # まっすぐ移動
                    if a[w-1] == '0':
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD
                    # 左へ移動
                    if a[w-1] == '1':
                        dp[h+1][w-1] += dp[h][w]
                        dp[h+1][w-1] %= MOD
                else:
                    # 左へ移動
                    if a[w-1] == '1':
                        dp[h+1][w-1] += dp[h][w]
                        dp[h+1][w-1] %= MOD
                    # 右へ移動
                    elif a[w] == '1':
                        dp[h+1][w+1] += dp[h][w]
                        dp[h+1][w+1] %= MOD
                    # まっすぐ移動
                    else:
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD

    print(dp[H][K-1])

                
main()