def main():
    S = input()

    dp = [0] * 13
    dp[0] = 1
    MOD = 10**9 + 7

    mul = 1

    for i in range(len(S)-1,-1,-1):
        nextdp = [0] * 13
        for j in range(13):
            if S[i] != '?':
                k = int(S[i])
                nextdp[(j+k*mul)%13] += dp[j]
                nextdp[(j+k*mul)%13] %= MOD
            else:
                for k in range(10):
                    nextdp[(j+k*mul)%13] += dp[j]
                    nextdp[(j+k*mul)%13] %= MOD
        dp = nextdp
        mul *= 10
        mul %= 13


    print(dp[5])


if __name__ == '__main__':
    main()