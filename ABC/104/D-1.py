def main():
    S = input()
    dp = [[0] * 4 for _ in range(len(S) + 5)]
    dp[0][0] = 1
    MOD = 10 ** 9 + 7

    for i in range(len(S)):
        for j in range(4):
            if S[i] == '?':
                dp[i+1][j] += dp[i][j] * 3
            else:
                dp[i+1][j] = dp[i][j]

            dp[i+1][j] %= MOD

        if S[i] == 'A' or S[i] == '?':
            dp[i+1][1] += dp[i][0]
            dp[i+1][1] %= MOD
        if S[i] == 'B' or S[i] == '?':
            dp[i+1][2] += dp[i][1]
            dp[i+1][2] %= MOD
        if S[i] == 'C' or S[i] == '?':
            dp[i+1][3] += dp[i][2]
            dp[i+1][3] %= MOD

    print(dp[len(S)][3])

if __name__ == "__main__":
    main()