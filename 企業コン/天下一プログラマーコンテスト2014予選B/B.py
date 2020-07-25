def main():
    N = int(input())
    S = input()
    T = [input() for _ in range(N)]
    T.sort()
    dp = [0] * (len(S) + 5)
    dp[0] = 1
    MOD = 10 ** 9 + 7
    for i in range(len(S) + 1):
        for t in T:
            if i - len(t) < 0:
                continue
            if S[i-len(t):i] == t:
                dp[i] += dp[i-len(t)]
                dp[i] %= MOD

    print(dp[len(S)] % MOD)


if __name__ == "__main__":
    main()