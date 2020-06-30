def main():
    s = input()
    tmp = s[0]
    cnt = 1
    ans = ""
    for i in range(1, len(s)):
        if tmp == s[i]:
            cnt += 1
        else:
            ans += tmp + str(cnt)
            tmp = s[i]
            cnt = 1
    ans += tmp + str(cnt)
    print(ans)


if __name__ == "__main__":
    main()