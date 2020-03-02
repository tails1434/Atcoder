def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    hand = [""] * N

    ans = 0
    for i, t in enumerate(T):
        if i <= K - 1:
            if t == 'r':
                hand[i] = 'p'
                ans += P
            if t == 's':
                hand[i] = 'r'
                ans += R
            if t == 'p':
                hand[i] = 's'
                ans += S
        else:
            if t == 'r':
                if hand[i - K] == 'p':
                    continue
                else:
                    hand[i] = 'p'
                    ans += P
            if t == 's':
                if hand[i - K] == 'r':
                    continue
                else:
                    hand[i] = 'r'
                    ans += R
            if t == 'p':
                if hand[i - K] == 's':
                    continue
                else:
                    hand[i] = 's'
                    ans += S

    print(ans)





if __name__ == "__main__":
    main()