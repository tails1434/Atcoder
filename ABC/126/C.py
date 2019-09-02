def main():
    N, K = map(int, input().split())

    ans = 0
    for i in range(1,N+1):
        cnt = 0
        tmp = i
        while tmp <= K - 1:
            cnt += 1
            tmp *= 2
        aa = (1 / (2 ** cnt)) * (1 / N)
        ans += aa

    print(ans)


main()