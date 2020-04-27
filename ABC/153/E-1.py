def main():
    H, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp = [float('inf')] * (H + 5)
    dp[0] = 0
    for i in range(H+1):
        for j in range(N):
            if i + A[j] >= H:
                dp[H] = min(dp[H], dp[i] + B[j])
            else:    
                dp[i + A[j]] = min(dp[i + A[j]], dp[i] + B[j])
    ans = dp[H]

    print(ans)

if __name__ == "__main__":
    main()