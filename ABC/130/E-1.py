def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    dp = [[0] * (M + 5) for _ in range(N + 5)]
    for i in range(N+1):
        dp[i][0] = 1
    for j in range(M+1):
        dp[0][j] = 1

    for i in range(1,N+1):
        for j in range(1,M+1):
            if S[i-1] == T[j-1]:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i-1][j]
            dp[i][j] += dp[i][j-1]
            dp[i][j] -= dp[i-1][j-1]
            dp[i][j] %= MOD

    print(dp[N][M])


if __name__ == "__main__":
    main()