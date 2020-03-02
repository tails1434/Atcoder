def main():
    H = int(input())
    if H == 1:
        print(1)
        exit()
    cnt = 1
    ans = 0
    while H > 1:
        H //= 2
        ans += cnt
        cnt *= 2

    print(ans + cnt)




if __name__ == "__main__":
    main()