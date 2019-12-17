def main():
    N, Ma, Mb = map(int, input().split())
    a = [0] * N
    b = [0] * N
    c = [0] * N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())

    dp = [[[float('inf')] * (405) for _ in range(405)] for _ in range(N + 5)]    
    dp[0][0][0] = 0

    for i in range(N):
        for j in range(401):
            for k in range(401):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]], dp[i][j][k] + c[i])

    ans = float('inf')
    for i in range(1,401):
        for j in range(1,401):
            if Ma * j == Mb * i:
                ans = min(ans, dp[N][i][j])

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
    


if __name__ == "__main__":
    main()