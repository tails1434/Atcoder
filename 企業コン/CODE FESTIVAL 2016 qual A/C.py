def main():
    S = input()
    K = int(input())
    ans = ""
    for i, s in enumerate(S):
        tmp = ord(s) - ord('a')
        if i == len(S) - 1:
            ans += chr((tmp + K) % 26 + ord('a'))
        elif s == 'a':
            ans += s
        elif 26 - tmp <= K:
            ans += 'a'
            K -= 26 - tmp
        else:
            ans += s

    print(ans)
            


if __name__ == "__main__":
    main()