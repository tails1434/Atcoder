import sys
import bisect
from collections import deque
sys.setrecursionlimit(4100000)
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)

    ans = [0] * (N + 1)
    LIS = [-1]
    
    def dfs(v, p = N):
        if A[v] > LIS[-1]:
            LIS.append(A[v])
            ans[v] = ans[p] + 1
            for u in edge[v]:
                if u == p:
                    continue
                dfs(u,v)
            LIS.pop()
        else:
            ans[v] = ans[p]
            idx = bisect.bisect_left(LIS, A[v])
            old = LIS[idx]
            LIS[idx] = A[v]
            for u in edge[v]:
                if u == p:
                    continue
                dfs(u,v)
            LIS[idx] = old
    dfs(0)
    for i in range(N):
        print(ans[i])

if __name__ == "__main__":
    main()