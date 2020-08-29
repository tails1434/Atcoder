def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        cnt = N // X
    else:
        cnt = (N // X) + 1

    print(cnt * T)

if __name__ == "__main__":
    main()