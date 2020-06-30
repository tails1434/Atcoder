def main():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = -(10**15)
    for i in range(2**10):
        tmp = []
        for j in range(10):
            if ((i >> j) & 1):
                tmp.append(j)
        if not tmp:
            continue
        score = 0
        for k in range(N):
            cnt = 0
            for l in range(10):
                if F[k][l] == 1 and l in tmp:
                    cnt += 1
            score += P[k][cnt]

        ans = max(ans, score)

    print(ans)
if __name__ == "__main__":
    main()