import sys
input = sys.stdin.readline

def main():
    N, M, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    C = list(map(int, input().split()))
    for _ in range(Q):
        s = list(map(int, input().split()))
        if s[0] == 1:
            x = s[1] - 1
            print(C[x])
            for v in edge[x]:
                C[v] = C[x]
        else:
            x = s[1] - 1 
            y = s[2]
            print(C[x])
            C[x] = y

if __name__ == "__main__":
    main()