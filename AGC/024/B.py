def main():
    N = int(input())
    P = list(int(input()) for _ in range(N))
    
    dp = [0] * (N + 1)
    for i in range(N-1,-1,-1):
        if P[i] == N:
            dp[P[i]] = 1
            continue
        if dp[P[i] + 1] == 0:
            dp[P[i]] = 1
        else:
            dp[P[i]] = dp[P[i] + 1] + 1
    print(N - max(dp))


if __name__ == "__main__":
    main()