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
    N = int(input())
    edge = [[] for i in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append([c,b])
        edge[b].append([c,a])
    Q, K = map(int, input().split())
    K -= 1
    d = dijkstra_heap(K,edge,N)
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1  
        print(d[x]+d[y])



if __name__ == "__main__":
    main()

