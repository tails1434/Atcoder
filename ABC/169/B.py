def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        exit()
    ans = 1
    for a in A:
        ans *= a
        if ans >= 10 ** 18 + 1:
            print(-1)
            exit()
    print(ans)

if __name__ == "__main__":
    main()