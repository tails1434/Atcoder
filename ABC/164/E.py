def main():
    N, M, S = map(int, input().split())

    cost = [[float('inf')] * N for _ in range(N)]
    time = [[float('inf')] * N for _ in range(N)]
    for _ in range(M):
        U, V, A, B = map(int, input().split())
        U -= 1
        V -= 1
        cost[U][V] = A
        cost[V][U] = A
        time[U][V] = B
        time[V][U] = B

    for i in range(N):
        time[i][i] = 0
    exchange_cost = [0] * N
    exchange_time = [0] * N
    for i in range(N):
        C, D = map(int, input().split())
        exchange_cost[i] = C
        exchange_time[i] = D


    for k in range(N):
        for i in range(N):
            for j in range(N):
                time[i][j] = min(time[i][j],time[i][k] + time[k][j])

    time2 = [[float('inf')] * N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):

if __name__ == "__main__":
    main()