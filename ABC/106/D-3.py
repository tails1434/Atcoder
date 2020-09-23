def main():
    N, M, Q = map(int, input().split())
    A = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        L, R = map(int, input().split())
        A[L][R] += 1
    
    S = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N+1):
        for j in range(N+1):
            S[i+1][j+1] = S[i][j+1] + S[i+1][j] - S[i][j] + A[i][j]
    for _ in range(Q):
        p, q = map(int, input().split())
        ans = S[q+1][q+1] - S[p][q+1] - S[q+1][p] + S[p][p]
        print(ans)

if __name__ == "__main__":
    main()