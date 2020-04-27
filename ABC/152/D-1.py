def main():
    N = int(input())
    cnt = [[0] * 10 for _ in range(10)]
    for i in range(1,N+1):
        tmp = str(i)
        top = int(tmp[0])
        end = int(tmp[-1])
        cnt[top][end] += 1
    ans = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a == d and b == c:
                        ans += cnt[a][b] * cnt[c][d]

    print(ans)



if __name__ == "__main__":
    main()