def main():
    N :list = list(map(lambda s: int(s), list(input())))
    K :int = int(input())
    L :int = len(N)
    dp :list = [[[0] * 5 for _ in range(2)] for _ in range(L + 5)]
    dp[0][0][0] = 1
    for i in range(L):
        for j in range(2):
            for k in range(K+1):
                if j == 0:
                    for x in range(N[i] + 1):
                        if x == N[i]:
                            if x == 0:
                                dp[i+1][0][k] += dp[i][0][k]
                            else:
                                dp[i+1][0][k+1] += dp[i][0][k]
                        else:
                            if x == 0:
                                dp[i+1][1][k] += dp[i][0][k]
                            else:
                                dp[i+1][1][k+1] += dp[i][0][k]
                else:
                    for x in range(10):
                        if x == 0:
                            dp[i+1][1][k] += dp[i][1][k]
                        else:
                            dp[i+1][1][k+1] += dp[i][1][k]

    print(dp[L][0][K]+dp[L][1][K])


    


if __name__ == "__main__":
    main()