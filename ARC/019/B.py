def main():
    S = list(input())
    len_S = len(S)
    match_S = [False] * len_S
    for i in range(len_S):
        if S[i] == S[-1-i]:
            match_S[i] = True
    ans = 0
    if match_S.count(False) == 0:
        if len_S % 2 == 0:
            ans = 25 * len_S
        else:
            ans = 25 * len_S - 25
    elif match_S.count(False) == 2:
        ans = 24 * 2 + 25 * (len_S - 2)
    else:
        ans = 25 * len_S
    print(ans)

if __name__ == "__main__":
    main()