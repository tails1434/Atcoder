from collections import deque

def main():
    N = int(input())
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    M = int(input())
    MOD = 10**9 + 7
    edge = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edge[x].append(y)
        edge[y].append(x)
    
    Q = deque([a])
    dist = [float('inf')] * N
    dp = [0] * N
    dp[a] = 1
    dist[a] = 0
    while Q:
        u = Q.popleft()
        if u == b:
            break
        for v in edge[u]:
            if dist[v] == float('inf'):
                dp[v] += dp[u]
                dp[v] %= MOD
                dist[v] = dist[u] + 1
                Q.append(v)
            elif dist[v] == dist[u] + 1:
                dp[v] += dp[u]
                dp[v] %= MOD
    print(dp[b] % MOD)




if __name__ == "__main__":
    main()