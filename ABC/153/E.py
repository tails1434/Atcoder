def main():
    H, N = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [float('inf')] * (H + max(A) + 5)
    dp[0] = 0
    for i in range(N):
        for j in range(H):
            dp[j + A[i]] = min(dp[j] + B[i], dp[j + A[i]])

    ans = float('inf')
    for i in range(H, H + max(A) + 1):
        ans = min(ans, dp[i])

    print(ans)


    
    


if __name__ == "__main__":
    main()