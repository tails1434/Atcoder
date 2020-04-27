def main():
    H = int(input())
    ans = 0
    cnt = 0
    while H > 1:
        H //= 2
        ans += 2 ** cnt
        cnt += 1
    ans += 2 ** cnt
    print(ans)



if __name__ == "__main__":
    main()