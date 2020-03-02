def main():
    N = int(input())
    S = input()
    dp = [[0] * 5005 for _ in range(5005)]
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j+1] + 1

    ans = 0
    for i in range(N):
        for j in range(N):
            if i >= j:
                continue
            now = min(dp[i][j], j-i)
            ans = max(ans, now)

    print(ans)
    


if __name__ == "__main__":
    main()