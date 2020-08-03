def main():
    K = int(input())
    if K % 2 == 0 and K % 5 == 0:
        print(-1)
        exit()
    ans = 0
    ten = 1
    mod = [0] * (10**6+5)
    for i in range(10**6):
        tmp = 7 * ten
        tmp %= K
        mod[i] = tmp
        ten *= 10
        ten %= K

    pre = 0   
    for i in range(10**6):
        pre += mod[i]
        if pre % K == 0:
            print(i+1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()