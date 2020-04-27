def main():
    N, M = map(int, input().split())
    A = list(map(int ,input().split()))
    ans = max(N - sum(A),-1)
    print(ans)


if __name__ == "__main__":
    main()