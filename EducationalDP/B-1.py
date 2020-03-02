def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [float('inf')] * (N + K)
    dp[0] = 0
    for i in range(N):
        for k in range(1,K+1):
            if i + k <= N - 1:
                dp[i+k] = min(dp[i+k], dp[i] + abs(H[i+k] - H[i]))
            else:
                break

    print(dp[N-1])



if __name__ == "__main__":
    main()