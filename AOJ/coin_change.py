def main():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    dp = [float('inf')] * (N + 5)
    dp[0] = 0
    for i in range(N+1):
        for c in C:
            if i + c > N + 1:
                continue
            dp[i+c] = min(dp[i+c], dp[i] + 1)

    print(dp[N])


if __name__ == "__main__":
    main()