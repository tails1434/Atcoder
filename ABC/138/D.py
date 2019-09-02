import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, p, tree, ans):
    for u in tree[v]:
        if u == p:
            continue
        ans[u] += ans[v]
        dfs(u, v, tree, ans)

def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)
    ans = [0] * N
    for i in range(Q):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    dfs(0, -1, tree, ans)

    print(*ans)

main()