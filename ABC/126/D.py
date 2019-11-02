import heapq
import sys

input = sys.stdin.readline

def dijkstra_heap(s,edge,N):
    d = [float('inf')] * N
    used = [True] * N
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist, a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
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

    for i in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append([w,v])
        edge[v].append([w,u])

    D = dijkstra_heap(0,edge,N)
    first = D[0]
    for d in D:
        if abs(d - first) % 2 == 0:
            print(0)
        else:
            print(1)

main()