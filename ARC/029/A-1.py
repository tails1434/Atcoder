def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = float('inf')
    for i in range(2**N):
        first = 0
        second = 0
        for j in range(N):
            if (i >> j) & 1:
                first += T[j]
            else:
                second += T[j]

        ans = min(ans, max(first,second))

    print(ans)
        


if __name__ == "__main__":
    main()