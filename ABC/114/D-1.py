from collections import defaultdict

def main():
    # 75 * 1
    # 25 * 3
    # 15 * 5
    # 5 * 5 * 3
    N = int(input())
    d = defaultdict(int)
    for n in range(1, N+1):
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                d[i] += 1
                n = n // i
        if n != 1:
            d[n] += 1

    d2 = 0
    d4 = 0
    d14 = 0
    d24 = 0
    d74 = 0
    for i in d.values():
        if i >= 2:
            d2 += 1
        if i >= 4:
            d4 += 1
        if i >= 14:
            d14 += 1
        if i >= 24:
            d24 += 1
        if i >= 74:
            d74 += 1

    ans = d74
    ans += d24 * (d2 - 1)
    ans += d14 * (d4 - 1)
    ans += (d4 * (d4 - 1) * (d2 - 2)) // 2

    print(ans)


if __name__ == "__main__":
    main()