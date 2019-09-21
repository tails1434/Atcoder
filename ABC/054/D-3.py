def main():
    N, Ma, Mb = map(int, input().split())
    a = [0] * N
    b = [0] * N
    c = [0] * N
    for i in range(N):
        a[i], b[i], c[i] = map(int, input().split())
    
    dp = [[[float('inf')] * 401 for _ in range(401)] for _ in range(41)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(N*10+1):
            for k in range(N*10+1):
                if dp[i][j][k] == float('inf'):
                    continue
                # 選ばない場合
                dp[i+1][j][k] = min(dp[i+1][j][k],dp[i][j][k])
                # 選んだ場合
                dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]],dp[i][j][k]+c[i])

    ans = float('inf')
    for i in range(1,N*10+1):
        for j in range(1,N*10+1):
            if Ma * j == Mb * i:
                ans = min(ans,dp[N][i][j])

    if ans == float('inf'):
        ans = -1

    print(ans)

main()