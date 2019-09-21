import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M, Q = map(int, input().split())
    S = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        L, R = map(int, input().split())
        S[L][R] += 1

    for i in range(1,N+1):
        for j in range(1,N+1):
            S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]

    for i in range(Q):
        p, q = map(int, input().split())
        ans = S[q][q] - S[q][p-1] - S[p-1][q] + S[p-1][p-1]
        print(ans)
    



main()