def main():
    N = input()
    if int(N) % 2 == 1:
        print(0)
        exit()
    cnt5 = 0
    for i in range(1,100):
        tmp =  int(N) // (5 ** i)
        cnt5 += tmp // 2
    print(cnt5)


if __name__ == "__main__":
    main()