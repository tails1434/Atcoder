from heapq import heappop, heappush, heapify

def main():
    N, M, S = map(int, input().split())
    S = min(S, 2500)
    edge = [[] for _ in range(N)]
    for _ in range(M):
        U, V, A, B = map(int, input().split())
        U -= 1
        V -= 1
        edge[U].append((V, A, B))
        edge[V].append((U, A, B))
    exchange = []
    for _ in range(N):
        C, D = map(int, input().split())
        exchange.append((C,D))

    dp = [[float('inf')] * 2510 for _ in range(N)]
    dp[0][S] = 0

    q = [(0,0,S)]
    while q:
        dist, v, money = heappop(q)
        if dp[v][money] < dist:
            continue
        for nv, fare, cost in edge[v]:
            nm = money - fare
            if nm < 0:
                continue
            if dp[nv][nm] > dp[v][money] + cost:
                dp[nv][nm] = dp[v][money] + cost
                heappush(q, (dp[nv][nm], nv, nm))
        
        nm = min(money+exchange[v][0], 2500)
        if dp[v][nm] > dp[v][money] + exchange[v][1]:
            dp[v][nm] = dp[v][money] + exchange[v][1]
            heappush(q, (dp[v][nm], v, nm))

    for i in range(1,N):
        print(min(dp[i]))


if __name__ == "__main__":
    main()