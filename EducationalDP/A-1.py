def main():
    N = int(input())
    H = list(map(int, input().split()))
    dp = [float('inf')] * (N + 5)
    dp[0] = 0
    for i in range(N):
        if i + 1 <= N - 1:
            dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1] - H[i]))
        if i + 2 <= N - 1:
            dp[i+2] = min(dp[i+2], dp[i] + abs(H[i+2] - H[i]))
    
    print(dp[N-1])

    

if __name__ == "__main__":
    main()