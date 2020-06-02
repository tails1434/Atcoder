from collections import deque

def main():
    N, K = map(int, input().split())
    edge = [[] for _ in range(N)]
    MOD = 10 ** 9 + 7
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    
    
    ans = K
    visited = [False] * N
    q = deque([[0,K]])
    while q:
        s, color = q.popleft()
        if visited[s]:
            continue
        visited[s] = True
        cnt = 0
        for v in edge[s]:
            if visited[v]:
                continue
            ans *= color - 1 - cnt
            ans %= MOD
            cnt += 1
            q.append([v,K-1])

    print(ans)

    



if __name__ == "__main__":
    main()