def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split())) + [0]
    T = list(map(int, input().split())) + [0]
    dp0 = [[0] * (M + 5) for _ in range(N + 5)]
    dp1 = [[0] * (M + 5) for _ in range(N + 5)]
    MOD = 10 ** 9 + 7
    dp0[0][0] = 1
    for i in range(N + 1):
        for j in range(M + 1):
            dp0[i+1][j] += dp0[i][j]
            dp0[i+1][j] %= MOD
            dp1[i][j] += dp0[i][j]
            dp1[i][j] %= MOD
            dp1[i][j+1] += dp1[i][j]
            dp1[i][j+1] %= MOD
            if S[i] == T[j]:
                dp0[i+1][j+1] += dp1[i][j]
                dp0[i+1][j+1] %= MOD

    ans = dp1[N][M] % MOD
    print(ans)



if __name__ == "__main__":
    main()