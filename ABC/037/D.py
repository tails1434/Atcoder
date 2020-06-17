
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
MOD = 10 ** 9 + 7
ans = 0
dp = [[-1] * W for _ in range(H)]


def dfs(h,w):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    if dp[h][w] != -1:
        return dp[h][w]
    else:
        ret = 1
        for i in range(4):
            nh = h + dy[i]
            nw = w + dx[i]

            if 0 <= nh < H and 0 <= nw < W:
                if A[h][w] >= A[nh][nw]:
                    continue
                ret += dfs(nh,nw)
                ret %= MOD

        dp[h][w] = ret
        return ret
                

for h in range(H):
    for w in range(W):
        ans += dfs(h,w)
        ans %= MOD

print(ans)
