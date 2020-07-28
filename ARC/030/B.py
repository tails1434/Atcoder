def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

def main():
    n, x = map(int, input().split())
    x -= 1
    h = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    def dfs(now, pre):
        cost = 0
        for v in edge[now]:
            if v == pre:
                continue
            cost_last = dfs(v, now)
            if cost_last > 0 or h[v] == 1:
                cost += cost_last + 2

        return cost

    ans = dfs(x, -1)
    print(ans)

if __name__ == "__main__":
    main()