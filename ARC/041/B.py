def main():
    N, M = map(int, input().split())
    B = [list(map(int, list(input()))) for _ in range(N)]
    C = [[str(0)] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if B[i][j] != 0:
                tmp = int(B[i][j])
                C[i+1][j] = str(tmp)
                if 0 <= i + 1 < N and 0 <= j - 1 < M:
                    B[i+1][j-1] -= tmp
                if 0 <= i + 2 < N:
                    B[i+2][j] -= tmp
                if 0 <= i + 1 < N and 0 <= j + 1 < M:
                    B[i+1][j+1] -= tmp
                B[i][j] = 0
    
    for c in C:
        print(''.join(c))

if __name__ == "__main__":
    main()