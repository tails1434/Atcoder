def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    cnt = [0] * 3
    for i in range(N):
        ans += S[i].count('AB')
        if S[i][0] == 'B' and S[i][-1] == 'A':
            cnt[0] += 1
        elif S[i][0] == 'B':
            cnt[1] += 1
        elif S[i][-1] == 'A':
            cnt[2] += 1

    if cnt[0] > 0:
        ans += cnt[0] - 1
        if not(cnt[1] == 0 and cnt[2] == 0):
            ans += 1
            ans += min(cnt[1],cnt[2])
    else:
        ans += min(cnt[1],cnt[2])

    print(ans)

    


if __name__ == "__main__":
    main()