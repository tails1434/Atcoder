def main():
    N, Wei = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    dp = [[0] * (Wei + 5) for _ in range(N + 5)]
    dp[0][Wei] = 0
    for i in range(N):
        for w in range(Wei+1):
            if w >= W[i]:
                dp[i+1][w] = max(dp[i][w-W[i]] + V[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

    print(dp[N][Wei])


if __name__ == "__main__":
    main()