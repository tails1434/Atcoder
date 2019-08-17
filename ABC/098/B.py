def main():
    N = int(input())
    S = input()

    ans = 0
    for i in range(1,N):
        L = list(set(S[:i]))
        R = list(set(S[i:]))
        cnt = 0
        for l in L:
            if l in R:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

main()