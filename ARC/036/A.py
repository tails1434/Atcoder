def main():
    N, K = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    S = [0] * (N + 1)
    for i in range(N):
        S[i+1] = S[i] + T[i]

    for i in range(N+1):
        if i + 3 <= N:
            tmp = S[i+3] - S[i]
            if tmp < K:
                print(i+3)
                exit()

    print(-1)

if __name__ == "__main__":
    main()