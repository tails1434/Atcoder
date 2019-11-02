def runlength(S):
    d = []
    cnt = 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            d.append(cnt)
            cnt = 1
        else:
            cnt += 1
    else:
        d.append(cnt)
    return d


def main():
    S = input()

    d = runlength(S)
    ans = [0] * len(S)
    pre = 0
    for i in range(0,len(d),2):
        tmp = d[i] + d[i+1]
        if d[i] % 2 == 0:
            ans[pre+d[i]-1] = tmp // 2
            ans[pre+d[i]] = tmp - ans[pre+d[i]-1]
        else:
            ans[pre+d[i]] = tmp // 2
            ans[pre+d[i]-1] = tmp - ans[pre+d[i]]

        pre += tmp

    print(*ans)


if __name__ == "__main__":
    main()