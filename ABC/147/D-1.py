def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    MOD = 10 ** 9 + 7
    for d in range(60):
        one = 0
        zero = 0
        for i in range(N):
            if A[i] & (1 << d):
                one += 1
            else:
                zero += 1

        ans += (2 ** d) * (one * zero)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()