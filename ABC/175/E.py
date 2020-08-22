import sys
input = sys.stdin.readline

def main():
    R, C, K = map(int, input().split())
    d = [[0] * (C + 5) for _ in range(R + 5)]
    dp = [[[0] * (4) for _ in range(C + 5)] for _ in range(R + 5)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        r -= 1
        c -= 1 
        d[r][c] = v

    for i in range(R):
        for j in range(C):
            for k in range(2,-1,-1):
                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k] + d[i][j])
            
            for k in range(4):
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][k])
                dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])

    ans = 0
    for k in range(4):
        ans = max(ans, dp[R-1][C-1][k])
    print(ans)

if __name__ == "__main__":
    main()