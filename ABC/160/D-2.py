def main():
    N, X, Y = map(int, input().split())
    tree = [[float('inf')] * N for _ in range(N)]
    ans = [0] * (N + 1)
    X -= 1
    Y -= 1
    for i in range(N):
        for j in range(i,N):
            dist = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[dist] += 1

    for i in range(1,N):
        print(ans[i])


if __name__ == "__main__":
    main()