def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    cnt = 0
    ans = 0
    for h in H:
        if cnt < K:
            cnt += 1
        else:
            ans += h
    print(ans)


if __name__ == "__main__":
    main()