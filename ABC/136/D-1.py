def runlegth(S):
    res = []
    cnt = 1
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
    res.append(cnt)
    return res

def main():
    S = input()
    L = runlegth(S)
    n = 0
    ans = [0] * len(S)
    flag = True
    cnt = 0
    for i in range(len(S)):
        if flag:
            if S[i] == 'L':
                tmp = L[n] + L[n+1]
                if cnt % 2 == 0:
                    ans[i-1] = tmp // 2 
                    ans[i] = tmp // 2 if tmp % 2 == 0 else tmp // 2 + 1
                else:
                    ans[i-1] = tmp // 2 if tmp % 2 == 0 else tmp // 2 + 1
                    ans[i] = tmp // 2
                n += 2
                flag = False
            else:
                cnt += 1
        else:
            if S[i] == 'R':
                flag = True
                cnt = 1

    print(*ans)


if __name__ == "__main__":
    main()