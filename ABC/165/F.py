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
    LIS = [A[0]]
    dist = [-1]*N
    dist[0] = 0
    ans = [0] * N
    ans[0] = 1
    queue = deque()
    queue.append((0,LIS))
    while queue:
        now, LIS_tmp = queue.popleft()
        d = dist[now]
        for i in edge[now]:
            tmp = LIS_tmp[:]
            if dist[i] > -1:
                continue
            dist[i] = d + 1
            if A[i] > tmp[-1]:
                tmp.append(A[i])
            else:
                tmp[bisect.bisect_left(tmp, A[i])] = A[i]
            queue.append((i,tmp))
            ans[i] = len(tmp)

    for i in range(N):
        print(ans[i])

    
if __name__ == "__main__":
    main()