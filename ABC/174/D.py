def main():
    N = int(input())
    C = list(input())
    ans = 0
    red = C.count('R')
    white = C.count('W')
    # 左に赤、右に白を寄せる場合
    cnt = 0
    for i in range(red):
        if C[i] == 'W':
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()