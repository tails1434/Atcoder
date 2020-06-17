import sys
sys.setrecursionlimit(200000)

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    
    dp = [[0] * 2 for _ in range(N+5)]
    MOD = 10 ** 9 + 7
    def dfs(i,c,p):
        if dp[i][c] == 0:
            ret = 1
            for v in edge[i]:
                if v == p:
                    continue
                if c == 0:
                    ret *= (dfs(v,0,i) + dfs(v,1,i))
                else:
                    ret *= dfs(v,0,i)
            dp[i][c] = ret % MOD
        return dp[i][c] % MOD

    ans = dfs(0,0,0) + dfs(0,1,0)
    print(ans % MOD)


if __name__ == "__main__":
    main()