def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    print(sum(D))
    print(max(0,2*max(D)-sum(D)))


if __name__ == "__main__":
    main()