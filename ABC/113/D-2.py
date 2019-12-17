def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 5)]
    dp[0][0] = 1
    MOD = 10 ** 9 + 7
    for h in range(H):
        for i in range(1 << W-1):
            a = str(bin(i))[2:].zfill(W-1)
            if a.count('11') >= 1:
                continue
            for w in range(W):
                if w == 0:
                    if a[w] == '1':
                        dp[h+1][w+1] += dp[h][w]
                        dp[h+1][w+1] %= MOD
                    elif a[w] == '0':
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD
                elif w == W - 1:
                    if a[w-1] == '1':
                        dp[h+1][w-1] += dp[h][w]
                        dp[h+1][w-1] %= MOD
                    elif a[w-1] == '0':
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD
                else:
                    if a[w-1] == '1':
                        dp[h+1][w-1] += dp[h][w]
                        dp[h+1][w-1] %= MOD
                    elif a[w] == '1':
                        dp[h+1][w+1] += dp[h][w]
                        dp[h+1][w+1] %= MOD
                    else:
                        dp[h+1][w] += dp[h][w]
                        dp[h+1][w] %= MOD

    print(dp[H][K-1])







if __name__ == "__main__":
    main()