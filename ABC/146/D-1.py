import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    ans = []
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append((b,i))
        edges[b].append((a,i))

    K = 0
    for i in range(N):
        K = max(K, len(edges[i]))

    visited = [False] * N

    def dfs(v, color):
        visited[v] = True
        for l, m in enumerate(edges[v]):
            if visited[m[0]]:
                continue
            color += 1
            color %= K
            ans.append((m[1],color))
            dfs(m[0], color)

    dfs(0,0)

    ans.sort()
    print(K)
    for a, b in ans:
        print(b+1)

if __name__ == "__main__":
    main()