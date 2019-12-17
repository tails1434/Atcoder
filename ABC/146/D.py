import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)

def main():
    N = int(input())
    d = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        d[a].append((b,i))
        d[b].append((a,i))

    ans = [0] * (N - 1) 

    def dfs(v, c, p):
        k = 1
        for i in range(len(d[v])):
            u = d[v][i][0]
            ei = d[v][i][1]
            if u == p:
                continue
            if k == c:
                k += 1
            ans[ei] = k
            k += 1
            dfs(u,ans[ei],v)
    
    dfs(0,-1,-1)
    print(max(ans))
    for a in ans:
        print(a)

        

if __name__ == "__main__":
    main()