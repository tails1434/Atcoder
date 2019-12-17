def main():
    S = input()
    N = len(S)
    if N % 2 == 0:
        first = list(S[:N//2])
        second = list(S[N//2:N])
        second.reverse()
        cnt = 0
        for i in range(N//2):
            if first[i] != second[i]:
                cnt += 1
    else:
        first = list(S[:N//2])
        second = list(S[N//2 + 1:N])
        second.reverse()
        cnt = 0
        for i in range(N//2):
            if first[i] != second[i]:
                cnt += 1


    print(cnt)


if __name__ == "__main__":
    main()