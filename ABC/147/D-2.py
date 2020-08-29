def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    L = 100
    for l in range(L):
        one = 0
        zero = 0
        for a in A:
            if (a & (1<<(L - l - 1))):
                one += 1
            else:
                zero += 1
        ans += (one * zero) * 2 ** (L - l - 1)
        ans %= MOD

    print(ans)
    


if __name__ == "__main__":
    main()