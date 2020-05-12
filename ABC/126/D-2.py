import heapq
import sys
sys.setrecursionlimit(4100000)
input = sys.stdin.readline

def dijkstra(s,N,edge):
    d = [float('inf')] * N
    used = [False] * N
    d[s] = 0
    used[s] = True
    edgelist = []
    for w, i in edge[s]:
        heapq.heappush(edgelist, w * (10**6) + i)
        # (w * (10**6) + i) // 10 ** 6 => 距離 w　が求められる
        # (w * (10**6) + i) % 10 ** 6 => 頂点 i　が求められる
    
    while edgelist:
        minedge = heapq.heappop(edgelist)
        if used[minedge%(10**6)]:
            continue
        v = minedge % (10 ** 6)
        d[v] = minedge // (10 ** 6)
        used[v] = True
        for w, i in edge[v]:
            if not used[i]:
                heapq.heappush(edgelist,(w+d[v])*(10**6)+i)

    return d


def main():
    N  = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append((w,v))
        edge[v].append((w,u))

    d = dijkstra(0,N,edge)

    for i in range(N):
        if d[i] % 2 == 0:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    main()