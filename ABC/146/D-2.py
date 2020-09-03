import sys
sys.setrecursionlimit(1000000)
def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append([b,i])
        edge[b].append([a,i])
    color = [0] * (N-1)
    def dfs(s,p,c):
        tmp_c = 1
        for v, num in edge[s]:
            if v == p:
                continue
            if tmp_c == c:
                tmp_c += 1
            color[num] = tmp_c
            dfs(v,s,tmp_c)
            tmp_c += 1
    dfs(0,-1,0)
    print(max(color))
    for c in color:
        print(c)


if __name__ == "__main__":
    main()