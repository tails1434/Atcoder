import sys
input = sys.stdin.readline

def main():
    N, M, Q = map(int, input().split())
    A = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        L, R = map(int, input().split())
        A[L][R] += 1

    for i in range(N+1):
        for j in range(1,N+1):
            A[i][j] += A[i][j-1]

    for j in range(N+1):
        for i in range(1,N+1):
            A[i][j] += A[i-1][j]

    for _ in range(Q):
        p, q = map(int, input().split())
        ans = A[q][q] - A[q][p-1] - A[p-1][q] + A[p-1][p-1]
        print(ans) 


if __name__ == "__main__":
    main()