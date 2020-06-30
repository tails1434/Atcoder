def main():
    N, M = map(int, input().split())
    dist = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = t
        dist[b][a] = t

    for i in range(N):
        dist[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    time = [0] * N
    for i in range(N):
        time[i] = max(dist[i])

    print(min(time))
 

if __name__ == "__main__":
    main()