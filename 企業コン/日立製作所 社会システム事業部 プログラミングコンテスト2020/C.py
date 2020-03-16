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
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    def dfs(edge, s, first,depth, visited, pairs):
        visited[s] = True
        if depth == 3:
            if first > s:
                first, s = s, first
            pairs.add((first,s))
            return
        res = set()
        for v in edge[s]:
            if visited[v]:
                continue
            dfs(edge, v, first, depth+1,visited,pairs)

    pairs = set()
    for i in range(N):
        visited = [False] * N
        dfs(edge,i, i, 0,visited, pairs)

    three = [[] for _ in range(N)]
    for i, j in pairs:
        three[i].append(i)
        three[j].append(i)

    if N % 3 == 0:
        cnt = (N // 3) + (N // 6)
    if N % 3 == 1:
        if (N - 1) % 6 == 0:
            cnt = (N // 3) + (N // 6)
        else:
            cnt = (N // 3) + (N // 6) + 1
    if N % 3 == 2:
        cnt = (N // 3) + (N // 6) + 1

    if len(pairs) > cnt:
        print(-1)
        exit()

    ans = [0] * N
    cnt_p = []
    for i in range(1,10,2):
        cnt_p.append([i,i+1])
    print(cnt_p)


if __name__ == "__main__":
    main()