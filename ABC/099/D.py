def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    cost = [[0] * C for j in range(3)]
    # 前処理
    for k in range(C):
        for i in range(N):
            for j in range(N):
                cost[(i+j)%3][k] += D[c[i][j]-1][k]

    # 全探索
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and j != k and k != i:
                    ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])

    print(ans)





main()