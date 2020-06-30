def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += int(S[i])
        else:
            ans -= int(S[i])

    print(ans)


if __name__ == "__main__":
    main()