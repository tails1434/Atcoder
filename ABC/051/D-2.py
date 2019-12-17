def warshal(N, d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def main():
    N, M = map(int, input().split())
    d = [[float('inf')] * N for _ in range(N)]
    edges = []

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c
        edges.append((a,b,c))

    warshal(N, d)

    cnt = 0
    for edge in edges:
        if d[edge[0]][edge[1]] != edge[2]:
            cnt += 1

    print(cnt)

    

if __name__ == "__main__":
    main()