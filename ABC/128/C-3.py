def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        k, *s = map(int, input().split())
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1<<N):
        on = []
        for j in range(N):
            if (i >> j) & 1:
                on.append(j+1)
        flag = True
        for m in range(M):
            cnt = 0
            for o in on:
                if o in S[m]:
                    cnt += 1
            if cnt % 2 != P[m]:
                flag = False
                break
            if not flag:
                break
        
        if flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()