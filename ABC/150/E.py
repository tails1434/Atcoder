def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    MOD = 10 ** 9 + 7
    two = [0] * (N + 1)
    two[0] = 1
    for i in range(N):
        two[i+1] = two[i] * 2
        two[i+1] %= MOD
    ans = 0
    for i in range(N):
        l = i
        r = N - 1 - i
        now = two[r]
        if r != 0:
            now += two[r-1] * r
        now *= two[l]
        now %= MOD
        now *= C[i]
        ans += now
        ans %= MOD

    ans *= two[N]
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()