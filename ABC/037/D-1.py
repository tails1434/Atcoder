import sys
sys.setrecursionlimit(10**9)

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    MOD = 10 ** 9 + 7
    dp = [[0] * W for _ in range(H)]
    dh = [1,0,-1,0]
    dw = [0,1,0,-1]
    def dfs(h,w):
        if dp[h][w] > 0:
            return dp[h][w]
        
        dp[h][w] = 1
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]

            if 0 <= nh < H and 0 <= nw < W and A[h][w] < A[nh][nw]:
                dp[h][w] += dfs(nh,nw)

        dp[h][w] %= MOD
        return dp[h][w]

    ans = 0
    for h in range(H):
        for w in range(W):
            ans += dfs(h,w)
            ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()