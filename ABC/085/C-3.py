def main():
    N, Y = map(int, input().split())
    for i in range(N+1):
        for j in range(N+1-i):
            tmp = 10000 * i + 5000 * j + 1000 * (N - i - j)
            if tmp == Y:
                print(i, j, N - i - j)
                exit()

    print(-1,-1,-1)



if __name__ == "__main__":
    main()