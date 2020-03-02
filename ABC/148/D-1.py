def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == cnt:
            cnt += 1
        else:
            ans += 1

    if A.count(1) == 0:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()