def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    ans = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            tmp = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            ans = max(ans, tmp)

    print(ans ** 0.5)
    


if __name__ == "__main__":
    main()