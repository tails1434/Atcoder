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
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    edge = [[] for _ in range(n)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        x -= 1
        y -= 1
        edge[x].append([d,y])
        edge[y].append([d,x])

    d1 = dijkstra_heap(s,edge,n)
    d2 = dijkstra_heap(t,edge,n)

    for i in range(n):
        if i == s or i == t:
            continue
        if d1[i] == 10**20 or d2[i] == 10**20:
            continue
        if d1[i] == d2[i]:
            print(i+1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()