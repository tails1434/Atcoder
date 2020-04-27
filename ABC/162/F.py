def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = A[0]
    dp[1] = A[1]
    for i in range(2,N):
        if i == 2:
            dp[i] = max(dp[i-2] + A[i], A[i])
        dp[i] = max(dp[i-2],dp[i-3]) + A[i]

    print(dp[N-1],dp[N-2])


if __name__ == "__main__":
    main()