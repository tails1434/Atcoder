def main():
    L = input()
    MOD = 10 ** 9 + 7
    dp = [[0] * 2 for _ in range(10 ** 6 + 5)]
    dp[0][0] = 1
    for i in range(len(L)):
        # a + b = 0
        if L[i] == '0':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][1] = (dp[i][0] + dp[i][1]) % MOD
        
        # a + b = 1
        if L[i] == '0':
            dp[i+1][1] += dp[i][1] * 2 % MOD
            dp[i+1][1] %= MOD
        else:
            dp[i+1][0] += dp[i][0] * 2 % MOD
            dp[i+1][1] += dp[i][1] * 2 % MOD
            dp[i+1][0] %= MOD
            dp[i+1][1] %= MOD

    ans = (dp[len(L)][0] + dp[len(L)][1]) % MOD
    print(ans)
    

if __name__ == "__main__":
    main()