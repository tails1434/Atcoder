def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
        exit()
    ans = (H // 2) * (W // 2)
    yoko = W // 2 if W % 2 == 0 else W // 2 + 1
    tate = H // 2 if H % 2 == 0 else H // 2 + 1
    ans += tate * yoko
    print(ans)



if __name__ == "__main__":
    main()