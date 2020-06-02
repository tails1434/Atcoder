def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[[0] * 3 for _ in range(S+5)] for _ in range(N+5)]
    dp[0][0][0] = 1
    MOD = 998244353
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j][0] += dp[i][j][0]
            dp[i+1][j][1] += dp[i][j][0] + dp[i][j][1] 
            dp[i+1][j][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]

            dp[i+1][j][0] %= MOD
            dp[i+1][j][1] %= MOD
            dp[i+1][j][2] %= MOD
            if j + A[i] <= S:
                dp[i+1][j+A[i]][1] += dp[i][j][0] + dp[i][j][1]
                dp[i+1][j+A[i]][2] += dp[i][j][0] + dp[i][j][1]
                dp[i+1][j+A[i]][1] %= MOD
                dp[i+1][j+A[i]][2] %= MOD

    print(dp[N][S][2])


if __name__ == "__main__":
    main()