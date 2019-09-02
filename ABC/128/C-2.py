def main():
    N, M = map(int, input().split())
    s = [[int(i) for i in input().split()][1:] for i in range(M)]
    p = list(map(int, input().split()))
    ans = 0

    for i in range(1<<N):
        for m in range(M):
            cnt = 0
            for j in s[m]:
                if i & (1<<j-1) != 0:
                    cnt += 1
            if cnt % 2 != p[m]:
                break
    else:
        ans += 1

    print(ans)

main()