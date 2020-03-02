def main():
    s = input()
    t = input()
    dp = [[0] * len(t) for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] == t[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(len(t)):
        if s[0] == t[i]:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i-1]

    for i in range(1,len(s)):
        for j in range(1,len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    


if __name__ == "__main__":
    main()