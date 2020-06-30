def main():
    N = int(input())
    S1 = input()
    S2 = input()
    MOD = 10 ** 9 + 7
    ans = 1
    cnt = 0
    while cnt < N:
        if cnt == 0:
            if S1[cnt] == S2[cnt]:
                ans *= 3
                cnt += 1
            else:
                ans *= 6
                cnt += 2
        else:
            if S1[cnt] == S2[cnt]:
                if S1[cnt-1] == S2[cnt-1]:
                    ans *= 2
                else:
                    ans *= 1
                cnt += 1
            else:
                if S1[cnt-1] == S2[cnt-1]:
                    ans *= 2
                else:
                    ans *= 3
                cnt += 2

        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()