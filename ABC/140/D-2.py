def runlength(S):
    cnt = 1
    res = []
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1

    res.append(cnt)
    return res


def main():
    N, K = map(int, input().split())
    S = input()
    A = runlength(S)
    ans = 0
    for a in A:
        a -= 1
        ans += a
    ans = min(N-1, ans + 2 * K)
    print(ans)


if __name__ == "__main__":
    main()