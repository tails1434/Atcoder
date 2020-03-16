def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
        exit()
    ans = 0
    ans += (W - (W // 2)) * (H - (H // 2))
    ans += (W // 2) * (H // 2) 

    print(ans)



if __name__ == "__main__":
    main()