def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    match = [0,2,5,5,4,5,6,3,7,6]
    dp = [-1] * (N + 10)
    dp[0] = 0
    for i in range(N):
        if dp[i] != -1:
            for a in A:
                dp[i+match[a]] = max(dp[i+match[a]], dp[i] * 10 + a)
        
    print(dp[N])


if __name__ == "__main__":
    main()