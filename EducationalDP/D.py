def main():
    N, W = map(int, input().split())
    w = [0] * N
    v = [0] * N
    for i in range(N):
        w[i], v[i] = map(int, input().split())

    dp = [[0] * (W + 5) for _ in range(N + 5)]
    
    for i in range(N):
        for j in range(W):
            print
            if j + w[i] <= W:
                dp[i+1][j + w[i]] = max(dp[i+1][j + w[i]], dp[i][j] + v[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    
    print(max(dp[N]))


if __name__ == "__main__":
    main()