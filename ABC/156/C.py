def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(1,101):
        tmp = 0
        for x in X:
            tmp += (x - i) ** 2
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()