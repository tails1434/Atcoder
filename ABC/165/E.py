def main():
    N, M = map(int, input().split())
    l = 1
    r = N - 1
    if N % 2 == 0:
        flag = True
        for i in range(M):
            if r - l <= N // 2 and flag:
                l += 1
                flag = False
            print(l,r)
            l += 1
            r -= 1
    else:
        for i in range(M):
            print(l,r)
            l += 1
            r -= 1

if __name__ == "__main__":
    main()