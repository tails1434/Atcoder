def main():
    '''
    A => 0
    C => 1
    G => 2
    T => 3
    '''
    N = int(input())
    MOD = 10 ** 9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(105)]
    
    dp[0][3][3][3] = 1

    for n in range(N):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for new in range(4):
                        if j == 0 and k == 2 and new == 1:
                            continue
                        if j == 2 and k == 0 and new == 1:
                            continue
                        if j == 0 and k == 1 and new == 2:
                            continue
                        if i == 0 and k == 2 and new == 1:
                            continue
                        if i == 0 and j == 2 and new == 1:
                            continue

                        dp[n+1][j][k][new] += dp[n][i][j][k]
                        dp[n+1][j][k][new] %= MOD

    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()