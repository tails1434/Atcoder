def main():
    N = list(map(int, list(input())))
    len_N = len(N)
    ans = 0
    pre = 0
    for i in range(len_N-1,-1,-1):
        tmp = N[i] + pre
        if tmp <= 4:
            ans += tmp
            pre = 0
        elif tmp >= 6:
            ans += 10 - tmp
            pre = 1
        else:
            if pre == 0:

    print(ans + pre)



if __name__ == "__main__":
    main()