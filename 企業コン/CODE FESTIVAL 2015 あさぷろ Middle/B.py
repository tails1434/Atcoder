def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

def main():
    N = int(input())
    S = input()
    ans = 10000
    for i in range(N):
        s = S[:i+1]
        t = S[i+1:]
        l = lcs(s,t)
        cnt = (len(s) - l) + (len(t) - l)
        ans = min(ans, cnt)

    print(ans)

if __name__ == "__main__":
    main()