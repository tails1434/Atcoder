def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    combo = [list(map(int, input().split())) for _ in range(M)] 
    ans = 0
    for i in range(2**N):
        tmp = []
        for j in range(N):
            if (i >> j) & 1:
                tmp.append(j+1)
        if len(tmp) != 9:
            continue
        score = 0
        for t in tmp:
            score += A[t-1]
        
        for c in combo:
            cnt = 0
            for k in range(2, len(c)):
                if (c[k] in tmp):
                    cnt += 1
            if cnt >= 3:
                score += c[0]

        ans = max(ans, score)

    print(ans)        



if __name__ == "__main__":
    main()