
def main():
    N, L = map(int, input().split())
    x = list(map(int, input().split()))
    T = list(map(int, input().split()))
    dp = [float('inf')] * (L + 10)
    h = [True] * (L+10)
    for i in x:
        h[i] = False
    dp[0] = 0
    for i in range(L+1):
        cnt = 0
        if not h[i]:
            cnt += 1
        dp[i+1] = min(dp[i+1],dp[i] + T[0] + T[2] * cnt)
        
        dp[i+1] = min(dp[i+1], dp[i] + T[0] // 2 + T[1] // 2 + T[2] * cnt)
        dp[i+2] = min(dp[i+2], dp[i] + T[0] + T[1] + T[2] * cnt)
        
        dp[i+1] = min(dp[i+1], dp[i] + T[0] // 2 + T[1] // 2 + T[2] * cnt)
        dp[i+2] = min(dp[i+2], dp[i] + T[0] // 2 + (3 * T[1]) // 2  + T[2] * cnt)
        dp[i+3] = min(dp[i+3], dp[i] + T[0] // 2 + (5 * T[1]) // 2  + T[2] * cnt)
        dp[i+4] = min(dp[i+4], dp[i] + T[0] + 3 * T[1] + T[2] * cnt)

    print(dp[L])


if __name__ == "__main__":
    main()