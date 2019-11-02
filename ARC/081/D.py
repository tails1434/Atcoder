def main():
    N = int(input())
    S1 = input()
    S2 = input()
    cnt = 0
    MOD = 10 ** 9 + 7
    i = 0
    while i < N:
        if i == 0:
            if S1[i] == S2[i]:
                cnt += 3
                cnt %= MOD
                i += 1
            else:
                cnt += 6
                cnt %= MOD
                i += 2
        else:
            if S1[i] == S2[i]:
                if S1[i-1] == S2[i-1]:
                    cnt *= 2
                    cnt %= MOD
                    i += 1
                else:
                    cnt *= 1
                    cnt %= MOD
                    i += 1
            else:
                if S1[i-1] == S2[i-1]:
                    cnt *= 2
                    cnt %= MOD
                    i += 2
                else:
                    cnt *= 3
                    cnt %= MOD
                    i += 2

    print(cnt)




if __name__ == "__main__":
    main()