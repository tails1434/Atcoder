def main():
    L = list(map(int,list(input())))
    MOD = 10 ** 9 + 7
    dp = [[0] * 2 for _ in range(len(L) + 5)]
    dp[0][0] = 1
    for i in range(len(L)):
        if L[i] == 0:
            dp[i+1][1] = 3 * dp[i][1]
            dp[i+1][0] = dp[i][0]
        else:
            dp[i+1][0] = 2 * dp[i][0]
            dp[i+1][1] = 3 * dp[i][1] + dp[i][0]

        dp[i+1][0] %= MOD
        dp[i+1][1] %= MOD

    print((dp[len(L)][0] + dp[len(L)][1]) % MOD)


if __name__ == "__main__":
    main()