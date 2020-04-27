import heapq
import sys
from collections import defaultdict

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
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        edge[i].append((1,i+1))
        edge[i+1].append((1,i))
    
    edge[X].append((1,Y))
    edge[Y].append((1,X))
    d = []
    for i in range(N):
        tmp = dijkstra_heap(i, edge, N)
        d.append(tmp)

    e = defaultdict(int)
    for i in range(N):
        for j in range(i,N):
            if i == j:
                continue
            e[d[i][j]] += 1

    for i in range(1,N):
        print(e[i])

if __name__ == "__main__":
    main()