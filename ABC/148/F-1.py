import heapq
import sys

input = sys.stdin.readline

def dijkstra_heap(s,edge,n):
    #始点sから各頂点への最短距離
    d = [10**20] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

def main():
    N, u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge = [[] for i in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        edge[A].append([1,B])
        edge[B].append([1,A])
    
    d1 = dijkstra_heap(u,edge, N)
    d2 = dijkstra_heap(v,edge, N)
    ans = 0
    for i in range(N):
        if d1[i] < d2[i]:
            ans = max(ans, d2[i]-1)

    print(ans)


if __name__ == "__main__":
    main()