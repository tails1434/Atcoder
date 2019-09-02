def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]

    sort_h = sorted(h, reverse=True)

    ans = float('inf')
    for i in range(N-K+1):
        tmp = sort_h[i] - sort_h[i + K - 1]
        if ans > tmp:
            ans = tmp

    print(ans)

main()