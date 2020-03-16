def main():
    N = int(input())
    if N % 2 == 1:
        print(0)
        exit()

    N //= 2
    ans = 0
    for i in range(1,100):
        tmp = N // (5 ** i)
        ans += tmp

    print(ans)



if __name__ == "__main__":
    main()