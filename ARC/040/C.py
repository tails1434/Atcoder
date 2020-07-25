def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = 0
    colored = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                colored[i][j] = True

    for i in range(N):
        for j in range(N-1,-1,-1):
            if colored[i][j]:
                cnt += 1
                if i + 1 < N:
                    for k in range(j,N):
                        colored[i+1][k] = False
                break


    print(cnt)


if __name__ == "__main__":
    main()